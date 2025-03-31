import random

from command import Command, BreakpointInfo
import breakpoint_generator

# infile – input analysis file made with PVOC
# outfile – output analysis file
# noise – Range 0 (no noise in spectrum) to 1 (spectrum saturated with noise)

# NOISE MAY VARY OVER TIME

def make_command():
    # breakpoint parameter
    parameter1 = ""
    parameter_list = [parameter1]
    return Command("blur noise", 1, parameter_list, BreakpointInfo(0, 0, 1))