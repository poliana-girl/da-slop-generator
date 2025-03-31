import random

from command import Command, BreakpointInfo
import breakpoint_generator

# blur suppress infile outfile N

#     N – the number of spectral components to reject

#         N may vary over time

def make_command():
    # breakpoint parameter
    parameter1 = ""
    parameter_list = [parameter1]
    return Command("blur suppress", 1, parameter_list, BreakpointInfo(0, 1, 100))