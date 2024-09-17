import random

from command import Command

#  Usage
# focus step inanalysisfile outanalysisfile timestep

# Typical command line:
# focus step raspdt.ana raspdtstep.ana 0.1
# Parameters

#     inanalysisfile – input analysis file
#     outanalysisfile – output analysis file
#     timestep duration of the steps. Must be >= the duration of two analysis frames. The value here is rounded internally to a multiple of analysis frame time. 

def make_command():
    parameter1 = random.uniform(0.001, 1)
    parameter_list = [parameter1]
    return Command("focus step", 1, parameter_list)