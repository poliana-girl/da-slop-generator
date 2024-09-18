import random

from command import Command

#  Usage
# hilite bltr infile outfile blurring tracing
# Parameters

#     infile – input analysis file made with PVOC
#     outfile – output analysis file
#     blurring – the number of windows over which to average the spectrum
#     tracing – the number of (loudest) channels to retain, in each window

#         blurring AND tracing may vary over time

def make_command():
    parameter1 = random.uniform(2,513)
    parameter2 = random.uniform(2,513)
    parameter_list = [parameter1, parameter2]
    return Command("hilite bltr", 2, parameter_list)