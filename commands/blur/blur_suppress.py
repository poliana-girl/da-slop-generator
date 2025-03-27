import random

from command import Command
import breakpoint_generator

# blur suppress infile outfile N

#     N – the number of spectral components to reject

#         N may vary over time

def make_command():
    parameter1 = breakpoint_generator.breakpoint_generator(1, 100)
    parameter_list = [parameter1]
    return Command("blur suppress", 1, parameter_list)