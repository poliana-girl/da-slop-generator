import random

from command import Command


# blur scatter infile outfile keep [-bblocksize] [-r] [-n]

#     keep – number of (randomly chosen) blocks to keep in each spectral window (Range: 1 to no. of chans.)
#     -bblocksize – frequency range of each block (default is width of 1 analysis channel. (Rounded internally to a multiple of channel width.)
#     -r number of blocks actually selected is randomised between 1 and keep
#     -n turn OFF normalisation of resulting sound

def make_command():
    parameter3_value = random.uniform(1, 513)
    parameter3 = "-r" + str(parameter3_value)
    parameter1 = random.uniform(2, parameter3_value)
    # print("blocks to keep:", parameter1)
    parameter2 = "-b" + str(random.uniform(50,70))
    
    
    # print("blocks per window:", parameter3)
    parameter_list = [parameter1, parameter2, parameter3]
    return Command("blur scatter", 3, parameter_list)

