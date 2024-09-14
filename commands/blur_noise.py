import random

from command import Command
import breakpoint_generator

# infile – input analysis file made with PVOC
# outfile – output analysis file
# noise – Range 0 (no noise in spectrum) to 1 (spectrum saturated with noise)

# NOISE MAY VARY OVER TIME

def make_command():
    parameter1 = breakpoint_generator.breakpoint_generator(0, 1)
    parameter_list = [parameter1]
    return Command("blur noise", 1, parameter_list)