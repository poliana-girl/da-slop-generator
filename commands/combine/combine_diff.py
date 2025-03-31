import random

from command import Command, BreakpointInfo
import breakpoint_generator

#  Usage
# combine diff infile infile2 outfile [-ccrossover] [-a]

#     -ccrossover – the amount of the 2nd spectrum subtracted from the 1st (Range: 0 to 1)

#         crossover may vary over time 

#     -a retain any subzero amplitudes produced (Default: set these to zero) 

def make_command():
    parameter1 = "-c" # + breakpoint_generator.breakpoint_generator(0, 1)
    parameter_list = [parameter1]
    return Command("combine diff", 1, parameter_list, BreakpointInfo(0, 0, 1))