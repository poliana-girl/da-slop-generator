import random

from command import Command
import breakpoint_generator

#  Usage
# hilite bltr infile outfile blurring tracing
# Parameters

#     infile – input analysis file made with PVOC
#     outfile – output analysis file
#     blurring – the number of windows over which to average the spectrum
#     tracing – the number of (loudest) channels to retain, in each window

#         blurring AND tracing may vary over time

def make_command():
    parameter1 = breakpoint_generator.breakpoint_generator(1,1000)
    parameter_list = [parameter1]
    return Command("hilite pluck", 1, parameter_list)