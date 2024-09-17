import random
import os

from command import Command
from commands.focus import focus

#  Usage
# focus freeze mode inanalysisfile outanalysisfile datafile

# Typical command line:
# focus freeze 3 raspdt.ana raspdtfrz.ana freeze.txt
# (See example datafiles in the text below.)
# Modes

#     1  freeze channel amplitudes
#     2  freeze channel frequencies
#     3  freeze channel amplitudes & frequencies

# Parameters

#     datafile – text file containing times at which the spectrum is frozen. These times may be preceded by character markers:

#         a use window here as freezewindow for spectrum AFTER this time
#         b use window here as freezewindow for spectrum BEFORE this time

#         Otherwise, times are end/start of freeze established at one of these markers.



def make_command():
    mode = random.randint(1, 3)
    
    parameter1 = focus_freeze_datafile_generator()
    parameter_list = [parameter1]
    return Command("focus freeze " + str(mode), 1, parameter_list)


def focus_freeze_datafile_generator():
    if not os.path.exists(focus.focus_datafile_directory_name):
        os.mkdir(focus.focus_datafile_directory_name)
    
    filename = focus.focus_datafile_directory_name + "/ff_datafile_" + str(random.randint(10000000, 99999999)) + ".txt"
    file = open(filename, "x")
    
    time = 0
    file.write("b")
    for i in range(80):
        time = time + random.randint(1, 15)
        if random.random() < 0.4 and time > 16:
            file.write("a")
        file.write(str(time))
        file.write("\n")
    
    file.close()
    return filename
