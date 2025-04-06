# PATHS INPUT FROM COMMAND LINE NEED TO BE INSIDE DOUBLE QUOTES FOR THIS TO WORK

import random
import sys
import os
import subprocess
from pathlib import Path

import utilities

first_arg = sys.argv[1]
segment_length = float(sys.argv[2])
number_of_segments = 1
segment_directory = "./segments/"

def make_split(sound):
    if utilities.is_audio_input_file(sound):
        current_time = utilities.get_formatted_date_time()
        segment_name = Path(sound).stem.replace(" ", "") + current_time + ".wav"
        
        # ffprobe -i <file> -show_entries format=duration -v quiet -of csv="p=0"
        sound_length = subprocess.check_output(f'ffprobe -i "{sound}" -show_entries format=duration -v quiet -of csv="p=0"', shell=True)
        sound_length = float(sound_length)
        start = random.uniform(0, sound_length - segment_length)
        end = start + segment_length
        utilities.mkdir_if_does_not_exist(segment_directory)
        subprocess.call(f'ffmpeg -i "{sound}" -ss {start} -to {end} {segment_directory + segment_name}', shell=True)
    else:
        print("file provided is not an audio file or does not exist!")
        sys.exit(-1)

if os.path.isdir(first_arg):
    if len(sys.argv) == 4:
        number_of_segments = int(sys.argv[3])
        directory = utilities.format_directory(first_arg)
        segment_directory = directory + "/segments/"
        for i in range(number_of_segments):
            chosen_sound = directory + utilities.choose_sound(directory)
            make_split(chosen_sound)
    else:
        print("missing argument! how many segments do you want to make?")
        sys.exit(-1)
else:
    sound = first_arg
    make_split(sound)