import random

from command import Command


#  Usage
# combine max infile infile2 [infile3 ...] outfile
# Parameters

#     infile, infile2 [infile3 ...]– arbitrary number of input analysis files
#     outfile– output analysis file 

def make_command():
    parameter_list = []
    return Command("combine max", 0, parameter_list)