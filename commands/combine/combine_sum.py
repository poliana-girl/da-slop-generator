import random

from command import Command
import breakpoint_generator

#  Usage
# combine sum infile infile2 outfile -ccrossover
# Parameters

#     -ccrossover crossover is the amount of 2nd spectrum which is added to the 1st (Range 0 to 1)

#         crossover may vary over time 

def make_command():
    parameter1 = "-c" + breakpoint_generator.breakpoint_generator(0, 1)
    parameter_list = [parameter1]
    return Command("combine sum", 1, parameter_list)