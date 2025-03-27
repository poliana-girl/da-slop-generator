import random

from command import Command
import breakpoint_generator

#  Usage

# specfold specfold 3 inanalfile outanalfile stt len seed [-a]
# Modes

#     1   Fold the spectrum.
#     2   Invert the spectrum.
#     3   Randomise the spectrum.

# Parameters

#     stt – lowest spectral channel to process (Range: >=1)
#     len – number of channels to process (>= 4); for folding (Mode 1) this must be an even number.
#     seed – (Mode 3) seed value sets a specific random permutation of channels. (Range: 1 to 64)
#     -a – process the amplitudes only. Default: process frequencies and amplitudes. 

def make_command():
    mode = 3
    parameter1 = random.uniform(1, 16)
    parameter2 = 4
    parameter3 = random.uniform(1, 64)
    
    parameter_list = [parameter1, parameter2, parameter3] 
    return Command("specfold specfold " + str(mode), 3, parameter_list)