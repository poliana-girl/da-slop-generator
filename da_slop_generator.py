# USAGE
# python da_slop_generator DIRECTORY NUM_SLOPS

import wave
import sys
import os
import subprocess
from pathlib import Path
import random
import soundfile as sf

import command

from date_time_format import get_formatted_date_time
import breakpoint_generator

# find a good way to differentiate between the ones that take 1 audio file and the ones that take 2. right now the only ones that take 2 are all the combines and formants vocode
from commands.blur import blur_avrg, blur_blur, caltrain_caltrain, blur_chorus, blur_drunk, blur_noise, blur_scatter, blur_shuffle, blur_spread, blur_suppress
from commands.combine import combine_cross, combine_diff, combine_interleave, combine_max, combine_mean, specsphinx_specsphinx, spectwin_spectwin, combine_sum
from commands.focus import superaccu_superaccu, focus_exag, focus_focus, focus_fold, focus_freeze, focus_step, specfold_specfold
from commands.formants import formants_vocode
from commands.hilite import hilite_bltr, glisten_glisten

# example_parameter_list = [30, 90]
# example_command = Command("example", 2, example_parameter_list)
# print(example_command)

# example_command2 = blur_avrg.make_command()
# print(example_command2)

# the first argument is a directory of input audio files.
directory = sys.argv[1]
# QoL thing just in case you forgot to add a slash to the end of the directory
if directory[-1] != "/":
    directory = directory + "/"

# the second argument is how many "slops" to generate, aka how many output audio files to generate
slops_to_generate = int(sys.argv[2])

# this folder is where the (channel-separated) input audio files are stored
original_channel_splits_folder = directory + "orig_channel_splits"

# TODO: ADD "directory +" to all of these and then go back and change every instance of "directory + XX_XX_directory_name" just to clean up the code
# this folder is where the (channel-separated) audio analysis files (.ana files, created from the above) are stored
original_ana_folder = directory + "orig_ana"

# this folder is where the (channel-separated) processed audio analysis files (.ana files, using the above as input) are stored (these are the products of the processing, which need to be converted back into .wav files for listening)
new_ana_folder = directory + "new_ana"

# this folder is where the (channel-separated) processed audio analysis files (converted .ana -> wav from the above) are stored
new_wav_folder = directory + "new_wav"

# this folder is where the (NON-channel-separated, properly merged) finished "slops"/output files are stored
finished_folder = directory + "FINISHED"

# creates a directory if it doesn't exist already
def mkdir_if_does_not_exist(path):
    if not os.path.exists(path): 
        os.mkdir(path)

# checks if a file is an audio file based on its extension. this can be adjusted to easily allow other formats of audio to be processed. anything you put here needs to be handleable by ffmpeg
def is_audio_input_file(file):
    if file.endswith('.wav') or file.endswith('.mp3') or file.endswith('.flac') or file.endswith('.m4a') or file.endswith('.ogg') or file.endswith('.aiff') or file.endswith('.opus'):
        return True
    else:
        return False

# splits each audio input file into 2 channels in wav format. it does not check whether a file is mono or not, so it does twice the work it needs to if a file is mono, but i'd have to change a lot of shit to make it work otherwise so i think it's fine for now
def create_splits(directory):
    mkdir_if_does_not_exist(original_channel_splits_folder)

    for file in os.listdir(directory):
        if is_audio_input_file(file):
            # split wavs file path (without extension or L/R markers, just to save some code duplication)
            split_wav_path = original_channel_splits_folder  + "/" + Path(file).stem

            split_wav_l = split_wav_path + "_L.wav"
            split_wav_r = split_wav_path + "_R.wav"

            if not os.path.isfile(split_wav_l) or not os.path.isfile(split_wav_r):
                # full ffmpeg command:
                # ffmpeg -i CHOSEN_FILE -filter_complex "[0:a]channelsplit=channel_layout=stereo[left][right]" -map [left] -ar 48000 -y SPLIT_WAV_L -map [right] -ar 48000 -y SPLIT_WAV_R
                subprocess.check_call(['ffmpeg', '-i', directory + file, '-filter_complex', "[0:a]channelsplit=channel_layout=stereo[left][right]", '-map', "[left]", "-ar", "48000", "-y", split_wav_l, '-map', "[right]", "-ar", "48000", "-y", split_wav_r])

# creates CDP analysis files (.ana) for each channel split (though it should be noted that this function is not explicitly AWARE of the relationship between channel splits. it just creates .ana files for all the files in the channel split folder)
def create_anas(directory):
    mkdir_if_does_not_exist(original_ana_folder)

    for file in os.listdir(original_channel_splits_folder):
        orig_ana = Path(file).stem + ".ana"
        if not os.path.isfile(original_ana_folder + "/" + orig_ana):
            subprocess.check_call(['pvoc', 'anal', '1', original_channel_splits_folder + "/" + file, original_ana_folder + "/" + orig_ana])

# chooses a random audio input file from the given directory
def choose_sound(directory):
    while True:
        choice = random.choice(os.listdir(directory))
        if is_audio_input_file(choice):
            return choice
        else:
            continue

# chooses twp random audio input file from the given directory (and verifies they are not the same file)
def choose_two_sounds(directory):
        while True:
            choice1 = random.choice(os.listdir(directory))
            if is_audio_input_file(choice1):
                choice2 = random.choice(os.listdir(directory))
                if choice1 != choice2 and is_audio_input_file(choice2):
                    return choice1, choice2
            else:
                continue

# this one exists because the audio input file is passed into the "execute command" functions (rather than passing both the left and right split .ana files into the function separately). this function simply reconstructs the file path and names of each split .ana file and returns them both 
def get_orig_ana_channel_splits_from_input_audio_file(sound):
    # this is the path to the ana files without "_L" or "_R" or an extension, to save some code duplication
    orig_ana_no_ext = original_ana_folder + "/" + Path(sound).stem
    
    orig_ana_l = orig_ana_no_ext + "_L.ana"
    orig_ana_r = orig_ana_no_ext + "_R.ana"
    return orig_ana_l, orig_ana_r

# exists for similar reasons as the above function, but for creating the path of the (not yet) PROCESSED .ana files instead. it's the filename passed into the command to make the new analysis file
# the command has to be passed into this one because the command's name becomes part of the final file name
def get_new_ana_channel_splits_from_input_audio_file(sound, command):
    # current time is used in file name to prevent overwriting other .ana files created from the same input audio files and processing method, but with different parameters
    current_time = get_formatted_date_time()

    # this is the path to the PROCESSED ana files without "_L" or "_R" or an extension, to save some code duplication. it also removes any spacesjust to keep things simple down the line
    new_ana_no_ext = new_ana_folder + "/" + Path(sound).stem + command.name.replace(" ", "") + current_time
    
    new_ana_l = new_ana_no_ext + "_L.ana"
    new_ana_r = new_ana_no_ext + "_R.ana"
    return new_ana_l, new_ana_r

# helper function for formatting commands properly in an array
def command_formatting_helper(command, ana_sequence_l, ana_sequence_r):
    command_split = command.name.split()
    command_l = command_split + ana_sequence_l
    command_r = command_split + ana_sequence_r
    for i in range(command.number_of_parameters):
        command_l.append(str(command.parameter_list[i]))
        command_r.append(str(command.parameter_list[i]))
    return command_l, command_r

# execute CDP program command type 1 (works on .ana files, takes 1 input analysis file, outputs 1 analysis file)
def execute_command_1(sound, command):
    mkdir_if_does_not_exist(new_ana_folder)

    # get names/paths to original channel split .anas
    orig_ana_l, orig_ana_r = get_orig_ana_channel_splits_from_input_audio_file(sound)

    # create names/paths for PROCESSED channel split .anas
    new_ana_l,  new_ana_r  = get_new_ana_channel_splits_from_input_audio_file(sound, command)

    # some shit i need to do in order to have the command's arguments split up, with each becoming a value in an array (which is how you have to input commands into subprocess.check_call)
    ana_sequence_l = [orig_ana_l, new_ana_l]
    ana_sequence_r = [orig_ana_r, new_ana_r]
    command_l, command_r = command_formatting_helper(command, ana_sequence_l, ana_sequence_r)

    # execute/run both commands for each channel
    subprocess.check_call(command_l)
    subprocess.check_call(command_r)

    return new_ana_l, new_ana_r

# execute CDP program command type 2 (works on .ana files, takes 2 input analysis files, outputs 1 analysis file)
def execute_command_2(directory, sound1, sound2, command):
    mkdir_if_does_not_exist(new_ana_folder)

    # get names/paths to original channel split .anas of the first sound
    orig_ana_l1, orig_ana_r1 = get_orig_ana_channel_splits_from_input_audio_file(sound1)
    # get names/paths to original channel split .anas of the second sound
    orig_ana_l2, orig_ana_r2 = get_orig_ana_channel_splits_from_input_audio_file(sound2)

    # create combined name of both input files (used for the final file name, because there's 2 sets of input .ana's and only 1 set of output .ana)
    combined_sound_name = Path(sound1).stem + Path(sound2).stem
    # create names/paths for PROCESSED channel split .anas
    new_ana_l, new_ana_r = get_new_ana_channel_splits_from_input_audio_file(combined_sound_name, command)

    # some shit i need to do in order to have the command's arguments split up, with each becoming a value in an array (which is how you have to input commands into subprocess.check_call)
    ana_sequence_l = [orig_ana_l1, orig_ana_l2, new_ana_l]
    ana_sequence_r = [orig_ana_r1, orig_ana_r2, new_ana_r]
    command_l, command_r = command_formatting_helper(command, ana_sequence_l, ana_sequence_r)

    # execute/run both commands for each channel
    subprocess.check_call(command_l)
    subprocess.check_call(command_r)

    return new_ana_l, new_ana_r

# from newly processed .ana files, synthesize them into (channel-split) wav files
def synth(new_ana_l, new_ana_r):
    mkdir_if_does_not_exist(new_wav_folder)

    # names of wav files to be created 
    new_wav_l = new_wav_folder + "/" + Path(new_ana_l).stem + ".wav"
    new_wav_r = new_wav_folder + "/" + Path(new_ana_r).stem + ".wav"

    # format and execute pvoc synth command
    subprocess.check_call(['pvoc', 'synth', new_ana_l, new_wav_l])
    subprocess.check_call(['pvoc', 'synth', new_ana_r, new_wav_r])
    return new_wav_l, new_wav_r

# finally, after all we've been through, merge the two synthesized wav files back into one wav file with 2 channels
def merge(new_wav_l, new_wav_r):
    mkdir_if_does_not_exist(finished_folder)
    
    finished_sound_name = Path(new_wav_l).stem[:-2].replace(" ", "") + ".wav"

    # full ffmpeg command:
    # ffmpeg -i left.wav -i right.wav -filter_complex "[0:a][1:a]join=inputs=2:channel_layout=stereo[a]" -map "[a]" output.wav
    subprocess.check_call(['ffmpeg', '-i', new_wav_l, '-i', new_wav_r, '-filter_complex', "[0:a][1:a]join=inputs=2:channel_layout=stereo[a]", '-map', "[a]", finished_folder + "/" + finished_sound_name])

# choose type 1 command
def choose_command_1():
    function_list = [
        blur_avrg.make_command, blur_blur.make_command, caltrain_caltrain.make_command, blur_chorus.make_command, blur_drunk.make_command, blur_noise.make_command, blur_scatter.make_command, blur_shuffle.make_command, blur_spread.make_command, blur_suppress.make_command,
        superaccu_superaccu.make_command, focus_exag.make_command, focus_focus.make_command, focus_fold.make_command, focus_freeze.make_command, focus_step.make_command, specfold_specfold.make_command,
        hilite_bltr.make_command, glisten_glisten.make_command
    ]
    return random.choice(function_list)()

# choose type 2 command
def choose_command_2():
    function_list = [
        combine_cross.make_command, combine_diff.make_command, combine_interleave.make_command, combine_max.make_command, combine_mean.make_command, specsphinx_specsphinx.make_command, spectwin_spectwin.make_command, combine_sum.make_command,
        formants_vocode.make_command
    ]
    return random.choice(function_list)()

def add_breakpoints(sound, command):
    if hasattr(random_command, "breakpoint_info"):
        # print(get_orig_wav_length(sound))
        sf_wav = sf.SoundFile(original_channel_splits_folder  + "/" + Path(sound).stem + "_L.wav")
        sound_length = sf_wav.frames / sf_wav.samplerate
        command.parameter_list[command.breakpoint_info.parameter_index] = command.parameter_list[command.breakpoint_info.parameter_index] + breakpoint_generator.breakpoint_generator(command.breakpoint_info.lower_bound, command.breakpoint_info.upper_bound, sound_length)

# MAIN PROGRAM STEPS

# 0. create split channels and create .ana files
create_splits(directory)
create_anas(directory)

for i in range(slops_to_generate):

    # FORK IN THE ROAD
    # first we need to choose whether to perform a command on a single sound, or on two different sounds
    # 70% chance of single sound, 30% chance of two sounds

    # set value to True to only test single sounds. set to False to only test two different sounds
    if True: # random.random() < 0.7:
        # SINGLE SOUND
        
        # 1. choose a file to use with a command
        sound = choose_sound(directory)

        # 2. choose a random command (comment this out when testing a certain command)
        # random_command = choose_command_1()
        # print(random_command)

        # uncomment to test out a certain command instead of a random one
        random_command = focus_focus.make_command()

        # 2.5 add breakpoints
        add_breakpoints(sound, random_command)

        # 3. execute that command
        test = execute_command_1(sound, random_command)

        # 4. convert resulting .ana files into .wav files for each channel
        test2 = synth(test[0], test[1])

        # 5. merge .wav files together into the final product
        merge(test2[0], test2[1])
        print(random_command)
    
    else:
        # TWO DIFFERENT SOUNDS

        # 1. choose two files to use with a command
        sound1, sound2 = choose_two_sounds(directory)

        # 2. choose a command
        # random_command = choose_command_2()

        # uncomment to test out a certain command instead of a random one
        random_command = combine_diff.make_command()

        # 2.5 add breakpoints
        print("go   ")
        if random_command.breakpoint_info is not None:
            print("gottem")
            sf_wav = sf.SoundFile(original_channel_splits_folder  + "/" + Path(sound1).stem + "_L.wav")
            sound_length = sf_wav.frames / sf_wav.samplerate
            random_command.parameter_list[0] = random_command.parameter_list[0] + breakpoint_generator.breakpoint_generator(random_command.breakpoint_info.lower_bound, random_command.breakpoint_info.upper_bound, sound_length)

        # 3. execute that command
        exec = execute_command_2(directory, sound1, sound2, random_command)

        # 4. convert resulting .ana files into .wav files for each channel
        test2 = synth(exec[0], exec[1])

        # 5. merge .wav files together into the final product
        merge(test2[0], test2[1])



