import random

from command import Command


#  Usage
# combine interleave infile infile2 [infile3 ...] outfile leafsize
# Parameters

#     infile(s) – an number of input files made with PVOC (at least two), which will be processed sequentially in the same order as given on the command line
#     outfile – output analysis file
#     leafsize – number of analysis windows in each leaf (group of windows)

def make_command():
    parameter1 = random.uniform(1, 50)
    parameter_list = [parameter1]
    return Command("combine interleave", 1, parameter_list)