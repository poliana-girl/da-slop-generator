# command format: 
# python manual_slop.py blur avrg infile outfile N

# should execute the command w/o you having to deal w/ analysis files or anything 

import sys
import os
from pathlib import Path
import subprocess

from date_time_format import get_formatted_date_time

def mkdir_if_does_not_exist(path):
    if not os.path.exists(path): 
        os.mkdir(path)

directory = "./.temp/"
mkdir_if_does_not_exist(directory)

# this folder is where the (channel-separated) input audio files are stored
original_channel_splits_folder = directory + "orig_channel_splits"
mkdir_if_does_not_exist(original_channel_splits_folder)

# TODO: ADD "directory +" to all of these and then go back and change every instance of "directory + XX_XX_directory_name" just to clean up the code
# this folder is where the (channel-separated) audio analysis files (.ana files, created from the above) are stored
original_ana_folder = directory + "orig_ana"
mkdir_if_does_not_exist(original_ana_folder)

# this folder is where the (channel-separated) processed audio analysis files (.ana files, using the above as input) are stored (these are the products of the processing, which need to be converted back into .wav files for listening)
new_ana_folder = directory + "new_ana"
mkdir_if_does_not_exist(new_ana_folder)

# this folder is where the (channel-separated) processed audio analysis files (converted .ana -> wav from the above) are stored
new_wav_folder = directory + "new_wav"
mkdir_if_does_not_exist(new_wav_folder)

# this folder is where the (NON-channel-separated, properly merged) finished "slops"/output files are stored
finished_folder = directory + "FINISHED"
mkdir_if_does_not_exist(finished_folder)

def create_splits(sound):
    # split wavs file path (without extension or L/R markers, just to save some code duplication)
    split_sound_no_ext = original_channel_splits_folder  + "/" + Path(sound).stem

    split_sound_l = split_sound_no_ext + "_L.wav"
    split_sound_r = split_sound_no_ext + "_R.wav"

    if not os.path.isfile(split_sound_l) or not os.path.isfile(split_sound_r):
        # full ffmpeg command:
        # ffmpeg -i CHOSEN_FILE -filter_complex "[0:a]channelsplit=channel_layout=stereo[left][right]" -map [left] -ar 48000 -y split_sound_L -map [right] -ar 48000 -y split_sound_R
        subprocess.check_call(['ffmpeg', '-i', sound, '-filter_complex', "[0:a]channelsplit=channel_layout=stereo[left][right]", '-map', "[left]", "-ar", "48000", "-y", split_sound_l, '-map', "[right]", "-ar", "48000", "-y", split_sound_r])
    
    return split_sound_l, split_sound_r

def create_ana(sound):
    orig_ana = original_ana_folder + "/" + Path(sound).stem + ".ana"
    if not os.path.isfile(orig_ana):
        subprocess.check_call(['pvoc', 'anal', '1', sound, orig_ana])
    return orig_ana

def synth(new_ana_l, new_ana_r):
    # names of wav files to be created 
    new_wav_l = new_wav_folder + "/" + Path(new_ana_l).stem + ".wav"
    new_wav_r = new_wav_folder + "/" + Path(new_ana_r).stem + ".wav"

    # format and execute pvoc synth command
    if not os.path.isfile(new_wav_l) or not os.path.isfile(new_wav_r):
        subprocess.check_call(['pvoc', 'synth', new_ana_l, new_wav_l])
        subprocess.check_call(['pvoc', 'synth', new_ana_r, new_wav_r])
    return new_wav_l, new_wav_r

def merge(new_wav_l, new_wav_r):
    finished_sound_name = Path(new_wav_l).stem[:-2].replace(" ", "") + ".wav"

    # full ffmpeg command:
    # ffmpeg -i left.wav -i right.wav -filter_complex "[0:a][1:a]join=inputs=2:channel_layout=stereo[a]" -map "[a]" output.wav
    subprocess.check_call(['ffmpeg', '-i', new_wav_l, '-i', new_wav_r, '-filter_complex', "[0:a][1:a]join=inputs=2:channel_layout=stereo[a]", '-map', "[a]", finished_folder + "/" + finished_sound_name])


sound1 = sys.argv[1]
split_sound1_l, split_sound1_r = create_splits(sound1)
split_ana1_l = create_ana(split_sound1_l)
split_ana1_r = create_ana(split_sound1_r)

# current_time = get_formatted_date_time()

# processed_ana1_l = new_ana_folder + "/" + Path(sound1).stem + current_time + "_L.ana"
# if not os.path.isfile(processed_ana1_l):
#     command_l = [sys.argv[1], sys.argv[2], split_ana1_l, processed_ana1_l] + sys.argv[4:]
#     subprocess.check_call(command_l)

# processed_ana1_r = new_ana_folder + "/" + Path(sound1).stem + current_time + "_R.ana"
# if not os.path.isfile(processed_ana1_r):
#     command_r = [sys.argv[1], sys.argv[2], split_ana1_r, processed_ana1_r] + sys.argv[4:]
#     subprocess.check_call(command_r)

# processed_sound1_l, processed_sound1_r = synth(processed_ana1_l, processed_ana1_r)
# merge(processed_sound1_l, processed_sound1_r)



# # right channel command
# subprocess.check_call(['pvoc', 'anal', '1', sound, original_ana_folder + "/" + orig_ana])