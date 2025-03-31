import random

from command import Command, BreakpointInfo
import breakpoint_generator

#  Usage
# focus exag inanalysisfile outanalysisfile exaggeration

# Typical command line:
# focus exag raspdt.ana raspdtexg.ana 0.5
# Parameters

#     exaggeration – < 1 widens troughs and narrows formants (focuses on the peaks); > 1 narrows troughs and widens formants (diffusing the peaks). Range: 0.00100 to 1000.

#         exaggeration may vary over time 

def make_command():
    parameter1 = ""
    parameter_list = [parameter1]
    
    if random.random() < 0.5:
        return Command("focus exag", 1, parameter_list, BreakpointInfo(0, 0.001, 1))
    else:
        return Command("focus exag", 1, parameter_list, BreakpointInfo(0, 1, 1000))