# not ready. for some reason it cares whether or not you have extra breakpoints beyond the sounds's length
# which means i would need to find a way to pipe the sounds length data into these command functions, which i'm too lazy to do atm

import random
import os

from command import Command
from commands.focus import focus

#  Usage
# focus hold inanalysisfile outanalysisfile datafile

# Typical command line:
# focus hold raspdt.ana raspdthold.ana holds.txt
# (See example datafile in the text below.)
# Parameters

# datafile – contains a list of paired times at which the spectrum is held and a hold-duration for each time. These data items must be paired correctly. 

def make_command():
    parameter1 = focus_hold_datafile_generator()
    parameter_list = [parameter1]

    return Command("focus hold", 1, parameter_list)


def focus_hold_datafile_generator():
    if not os.path.exists(focus.focus_datafile_directory_name):
        os.mkdir(focus.focus_datafile_directory_name)
    
    filename = focus.focus_datafile_directory_name + "/fh_datafile_" + str(random.randint(10000000, 99999999)) + ".txt"
    file = open(filename, "x")
    
    time = 0

    for i in range(30):
        time = time + random.randint(1, 15)
        file.write(str(time))
        file.write(" ")
        file.write(str(random.uniform(0.1, 7)))
        file.write("\n")
    
    file.close()
    return filename
