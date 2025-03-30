# USAGE
# python da_slop_generator DIRECTORY NUM_SLOPS

import wave
import sys
import os
import subprocess
from pathlib import Path
import random
import datetime

import command


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

# the second argument is how many "slops" to generate, aka how many output audio files to generate
slops_to_generate = int(sys.argv[2])

# this folder is where the (channel-separated) input audio files are stored
original_channel_splits_folder = directory + "orig_channel_splits"

# TODO: ADD "directory +" to all of these and then go back and change every instance of "directory + XX_XX_directory_name" just to clean up the code
# this folder is where the (channel-separated) audio analysis files (.ana files, created from the above) are stored
original_ana_folder = directory + "orig_ana"

# this folder is where the (channel-separated) processed audio analysis files (.ana files, using the above as input) are stored (these are the products of the processing, which need to be converted back into .wav files for listening)
new_ana_folder = "new_ana"

# this folder is where the (channel-separated) processed audio analysis files (converted .ana -> wav from the above) are stored
new_wav_directory_name = "new_wav"

# this folder is where the (NON-channel-separated, properly merged) finished "slops"/output files are stored
merged_wav_directory_name = "FINISHED"

def mkdir_if_does_not_exist(path):
    if not os.path.exists(path): 
        os.mkdir(path)

def is_audio_input_file(file):
    if file.endswith('.wav') or file.endswith('.mp3') or file.endswith('.flac') or file.endswith('.m4a') or file.endswith('.ogg') or file.endswith('.aiff') or file.endswith('.opus'):
        return True
    else:
        return False

def create_splits(directory):
    mkdir_if_does_not_exist(original_channel_splits_folder)

    for file in os.listdir(directory):
        if is_audio_input_file(file):
            orig_left_channel_wav =  original_channel_splits_folder  + "/" + Path(file).stem + "_L.wav"
            orig_right_channel_wav = original_channel_splits_folder  + "/" + Path(file).stem + "_R.wav"
            if not os.path.isfile(orig_left_channel_wav) or not os.path.isfile(orig_right_channel_wav):
                subprocess.check_call(['ffmpeg', '-i', directory + file, '-filter_complex', "[0:a]channelsplit=channel_layout=stereo[left][right]", '-map', "[left]", "-ar", "48000", orig_left_channel_wav, '-map', "[right]", "-ar", "48000", orig_right_channel_wav])
    
def create_anas(directory):
    mkdir_if_does_not_exist(original_ana_folder)

    for file in os.listdir(original_channel_splits_folder):
        orig_ana = Path(file).stem + ".ana"
        if not os.path.isfile(original_ana_folder + "/" + orig_ana):
            subprocess.check_call(['pvoc', 'anal', '1', original_channel_splits_folder + "/" + file, original_ana_folder + "/" + orig_ana])

def choose_sound(directory):
    while True:
        choice = random.choice(os.listdir(directory))
        if is_audio_input_file(choice):
            return choice
        else:
            continue

def choose_two_sounds(directory):
        while True:
            choice1 = random.choice(os.listdir(directory))
            if is_audio_input_file(choice1):
                choice2 = random.choice(os.listdir(directory))
                if choice1 != choice2 and is_audio_input_file(choice2):
                    return choice1, choice2
            else:
                continue
    

def execute_command(directory, sound, command):
    # final = [command.name, Path(directory + sound).stem + "_L.ana", Path(directory + sound).stem + command.name.replace(" ", "_") + "_L.ana"]
    mkdir_if_does_not_exist(directory + new_ana_directory_name)

    current_time = datetime.datetime.now().strftime("%I-%M-%S%p") 
    orig_ana_l = original_ana_folder + "/" + Path(sound).stem + "_L.ana"
    new_ana_l = new_ana_folder + "/" + Path(sound).stem + "_" + command.name.replace(" ", "_")  + "_" + current_time + "_L.ana"
    orig_ana_r = original_ana_folder + "/" + Path(sound).stem + "_R.ana"
    new_ana_r = new_ana_folder + "/" + Path(sound).stem + "_" + command.name.replace(" ", "_")  + "_" + current_time + "_R.ana"

    command_split = command.name.split()
    command_l = command_split + [orig_ana_l, new_ana_l]
    command_r = command_split + [orig_ana_r, new_ana_r]

    for i in range(command.number_of_parameters):
        command_l.append(str(command.parameter_list[i]))
        command_r.append(str(command.parameter_list[i]))

    subprocess.check_call(command_l)
    subprocess.check_call(command_r)

    return new_ana_l, new_ana_r

def execute_command2(directory, sound1, sound2, command):
    # final = [command.name, Path(directory + sound).stem + "_L.ana", Path(directory + sound).stem + command.name.replace(" ", "_") + "_L.ana"]
    mkdir_if_does_not_exist(directory + new_ana_directory_name)

    current_time = datetime.datetime.now().strftime("%I-%M-%S%p") 
    orig_ana_l1 = original_ana_folder + "/" + Path(sound1).stem + "_L.ana"
    orig_ana_r1 = original_ana_folder + "/" + Path(sound1).stem + "_R.ana"

    orig_ana_l2 = original_ana_folder + "/" + Path(sound2).stem + "_L.ana"
    orig_ana_r2 = original_ana_folder + "/" + Path(sound2).stem + "_R.ana"

    new_ana_l = new_ana_folder + "/" + Path(sound1).stem + Path(sound2).stem + "_" + command.name.replace(" ", "_")  + "_" + current_time + "_L.ana"
    new_ana_r = new_ana_folder + "/" + Path(sound1).stem + Path(sound2).stem + "_" + command.name.replace(" ", "_")  + "_" + current_time + "_R.ana"

    command_split = command.name.split()
    command_l = command_split + [orig_ana_l1, orig_ana_l2, new_ana_l]
    command_r = command_split + [orig_ana_r1, orig_ana_r2, new_ana_r]

    for i in range(command.number_of_parameters):
        command_l.append(str(command.parameter_list[i]))
        command_r.append(str(command.parameter_list[i]))

    subprocess.check_call(command_l)
    subprocess.check_call(command_r)

    return new_ana_l, new_ana_r


def synth(left_channel, right_channel):
    if not os.path.exists(directory + new_wav_directory_name):
        os.mkdir(directory + new_wav_directory_name)
    new_wav_l = directory + new_wav_directory_name + "/" + Path(left_channel).stem + ".wav"
    new_wav_r = directory + new_wav_directory_name + "/" + Path(right_channel).stem + ".wav"
    subprocess.check_call(['pvoc', 'synth', left_channel, new_wav_l])
    subprocess.check_call(['pvoc', 'synth', right_channel, new_wav_r])
    return new_wav_l, new_wav_r

def merge(left_channel, right_channel):
    if not os.path.exists(directory + merged_wav_directory_name):
        os.mkdir(directory + merged_wav_directory_name)
    
    finished_sound_name = Path(left_channel).stem[:-2].replace(" ", "") + ".wav"

    # original command:
    # ffmpeg -i left.wav -i right.wav -filter_complex "[0:a][1:a]join=inputs=2:channel_layout=stereo[a]" -map "[a]" output.wav
    subprocess.check_call(['ffmpeg', '-i', left_channel, '-i', right_channel, '-filter_complex', "[0:a][1:a]join=inputs=2:channel_layout=stereo[a]", '-map', "[a]", directory + merged_wav_directory_name + "/" + finished_sound_name])

# picks an effect out of the ones that take 1 input audio file
def choose_function():
    function_list = [
        blur_avrg.make_command, blur_blur.make_command, caltrain_caltrain.make_command, blur_chorus.make_command, blur_drunk.make_command, blur_noise.make_command, blur_scatter.make_command, blur_shuffle.make_command, blur_spread.make_command, blur_suppress.make_command,
        superaccu_superaccu.make_command, focus_exag.make_command, focus_focus.make_command, focus_fold.make_command, focus_freeze.make_command, focus_step.make_command, specfold_specfold.make_command,
        hilite_bltr.make_command, glisten_glisten.make_command
    ]
    return random.choice(function_list)()

# picks an effect out of the ones that take 2 input audio files
def choose_function2():
    function_list = [
        combine_cross.make_command, combine_diff.make_command, combine_interleave.make_command, combine_max.make_command, combine_mean.make_command, specsphinx_specsphinx.make_command, spectwin_spectwin.make_command, combine_sum.make_command,
        formants_vocode.make_command
    ]
    return random.choice(function_list)()


# TODO: 
# make more command types; will probably need some trial and error on my part to find out what values u can shove into a command
# consider taking out all the subprocess shit and just outputting all the commands into a bash script that u can run whenever
# also it looks like the command format isn't ALWAYS command infile outfile param1 param2 sometimes there are 2 infiles.

# NOTE: sounds must be .wav files
# 0. split channels and create .ana files
create_splits(directory)
create_anas(directory)

# MAIN LOOP
for i in range(slops_to_generate):

    # FORK IN THE ROAD
    # first we need to choose whether to perform a command on a single sound, or on two different sounds
    # 70% chance of single sound, 30% chance of two sounds

    # set value to True to only test single sounds. set to False to only test two different sounds
    if random.random() < 0.7:
        # SINGLE SOUND
        
        # 1. choose a file to use with a command
        sound = choose_sound(directory)

        # 2. choose a random command (comment this out when testing a certain command)
        random_command = choose_function()
        print(random_command)

        # uncomment to test out a certain command instead of a random one
        # random_command = xxx.make_command()

        # 3. execute that command
        test = execute_command(directory, sound, random_command)

        # 4. convert resulting .ana files into .wav files for each channel
        test2 = synth(test[0], test[1])

        # 5. merge .wav files together into the final product
        merge(test2[0], test2[1])
    
    else:
        # TWO DIFFERENT SOUNDS

        # 1. choose two files to use with a command
        sound1, sound2 = choose_two_sounds(directory)

        # 2. choose a command
        random_command = choose_function2()

        # uncomment to test out a certain command instead of a random one
        # random_command = formants_vocode.make_command()

        # 3. execute that command
        exec = execute_command2(directory, sound1, sound2, random_command)

        # 4. convert resulting .ana files into .wav files for each channel
        test2 = synth(exec[0], exec[1])

        # 5. merge .wav files together into the final product
        merge(test2[0], test2[1])



