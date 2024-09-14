import wave
import sys
import os
import subprocess
from pathlib import Path
import random
import datetime

import command

from commands import blur_avrg, blur_blur, caltrain_caltrain, blur_chorus, blur_drunk, blur_noise, blur_scatter, blur_shuffle

# example_parameter_list = [30, 90]
# example_command = Command("example", 2, example_parameter_list)
# print(example_command)

# example_command2 = blur_avrg.make_command()
# print(example_command2)


directory = sys.argv[1]
slops_to_generate = sys.argv[2]

original_channel_splits_directory_name = "orig_channel_splits"
original_ana_directory_name = "orig_ana"
new_ana_directory_name = "new_ana"
new_wav_directory_name = "new_wav"
merged_wav_directory_name = "FINISHED"

def create_splits(directory):
    if not os.path.exists(directory + original_channel_splits_directory_name):
        os.mkdir(directory + original_channel_splits_directory_name)

    for file in os.listdir(directory):
        if file.endswith('.wav') or file.endswith('.mp3') or file.endswith('.flac') or file.endswith('.m4a') or file.endswith('.ogg') or file.endswith('.aiff'):
            orig_left_channel_wav =  directory + original_channel_splits_directory_name + "/" + Path(file).stem + "_L.wav"
            orig_right_channel_wav = directory + original_channel_splits_directory_name + "/" + Path(file).stem + "_R.wav"
            if not os.path.isfile(orig_left_channel_wav) or not os.path.isfile(orig_left_channel_wav):
                subprocess.check_call(['ffmpeg', '-i', directory + file, '-filter_complex', "[0:a]channelsplit=channel_layout=stereo[left][right]", '-map', "[left]", orig_left_channel_wav, '-map', "[right]", orig_right_channel_wav])
    
def create_anas(directory):
    if not os.path.exists(directory + original_ana_directory_name):
        os.mkdir(directory + original_ana_directory_name)
    
    for file in os.listdir(directory + original_channel_splits_directory_name):
        orig_ana = Path(file).stem + ".ana"
        if not os.path.isfile(directory + original_ana_directory_name + "/" + orig_ana):
            subprocess.check_call(['pvoc', 'anal', '1', directory + original_channel_splits_directory_name + "/" + file, directory + original_ana_directory_name + "/" + orig_ana])

def choose_sound(directory):
    while True:
        choice = random.choice(os.listdir(directory))
        if choice.endswith(".wav"):
            return choice
        else:
            continue
    

def execute_command(directory, sound, command):
    # final = [command.name, Path(directory + sound).stem + "_L.ana", Path(directory + sound).stem + command.name.replace(" ", "_") + "_L.ana"]
    if not os.path.exists(directory + new_ana_directory_name):
        os.mkdir(directory + new_ana_directory_name)

    current_time = datetime.datetime.now().strftime("%I:%M:%S%p") 
    orig_ana_l = directory + original_ana_directory_name + "/" + Path(sound).stem + "_L.ana"
    new_ana_l = directory + new_ana_directory_name + "/" + Path(sound).stem + "_" + command.name.replace(" ", "_")  + "_" + current_time + "_L.ana"
    orig_ana_r = directory + original_ana_directory_name + "/" + Path(sound).stem + "_R.ana"
    new_ana_r = directory + new_ana_directory_name + "/" + Path(sound).stem + "_" + command.name.replace(" ", "_")  + "_" + current_time + "_R.ana"

    command_split = command.name.split()
    command_l = command_split + [orig_ana_l, new_ana_l]
    command_r = command_split + [orig_ana_r, new_ana_r]

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
    
def choose_function():
    function_list = [blur_avrg.make_command, blur_blur.make_command, caltrain_caltrain.make_command, blur_chorus.make_command, blur_drunk.make_command, blur_noise.make_command, blur_scatter.make_command, blur_shuffle.make_command]
    return random.choice(function_list)()


# TODO: 
# make more command types; will probably need some trial and error on my part to find out what values u can shove into a command
# consider taking out all the subprocess shit and just outputting all the commands into a bash script that u can run whenever
# also it looks like the command format isn't ALWAYS command infile outfile param1 param2 sometimes there are 2 infiles.


create_splits(directory)
create_anas(directory)

for i in range(int(slops_to_generate)):

    sound = choose_sound(directory)

    # random_command = choose_function()

    # uncomment to test out a certain command instead of a random one
    random_command = blur_shuffle.make_command()

    test = execute_command(directory, sound, random_command)

    test2 = synth(test[0], test[1])

    merge(test2[0], test2[1])

