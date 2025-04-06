import datetime
import os
import random

# formatted date and time for output file names and breakpoints
def get_formatted_date_time():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# checks if a file is an audio file based on its extension. this can be adjusted to easily allow other formats of audio to be processed. anything you put here needs to be handleable by ffmpeg
def is_audio_input_file(file):
    if file.endswith('.wav') or file.endswith('.mp3') or file.endswith('.flac') or file.endswith('.m4a') or file.endswith('.ogg') or file.endswith('.aiff') or file.endswith('.opus'):
        return True
    else:
        return False

# creates a directory if it doesn't exist already
def mkdir_if_does_not_exist(path):
    if not os.path.exists(path): 
        os.mkdir(path)

# chooses a random audio input file from the given directory
def choose_sound(directory):
    while True:
        choice = random.choice(os.listdir(directory))
        if is_audio_input_file(choice):
            return choice
        else:
            continue

# QoL thing just in case you forgot to add a slash to the end of the directory
def format_directory(directory):
    if directory[-1] != "/":
        directory = directory + "/" 
    return directory