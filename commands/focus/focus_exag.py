import random

from command import Command
import breakpoint_generator

#  Usage
# focus exag inanalysisfile outanalysisfile exaggeration

# Typical command line:
# focus exag raspdt.ana raspdtexg.ana 0.5
# Parameters

#     exaggeration – < 1 widens troughs and narrows formants (focuses on the peaks); > 1 narrows troughs and widens formants (diffusing the peaks). Range: 0.00100 to 1000.

#         exaggeration may vary over time 

def make_command():
    if random.random() < 0.5:
        parameter1 = breakpoint_generator.breakpoint_generator(0.001, 1)
    else:
        parameter1 = breakpoint_generator.breakpoint_generator(1, 1000)
    
    parameter_list = [parameter1]
    return Command("focus exag", 1, parameter_list)