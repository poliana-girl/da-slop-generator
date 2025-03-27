import random

from command import Command
import breakpoint_generator

#  Usage
# focus fold inanalysisfile outanalysisfile lofrq hifrq -x

# Typical command line:
# focus fold raspdt.ana raspdtfold.ana 100 900 -x
# Parameters

#     lofrq lowest frequency of range into which the spectrum is folded
#     hifrq highest frequency of range into which the spectrum is folded
#     -x fuller spectrum

#         lofrq and hifrq may vary over time


def make_command():
    middle = random.uniform(2, 23999)
    parameter1 = breakpoint_generator.breakpoint_generator(1, middle)
    parameter2 = breakpoint_generator.breakpoint_generator(middle + 1, 24000)
    parameter3 = "-x"
    
    parameter_list = [parameter1, parameter2, parameter3]
    return Command("focus fold", 3, parameter_list)