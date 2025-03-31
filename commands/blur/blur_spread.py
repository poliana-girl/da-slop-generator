import random

from command import Command, BreakpointInfo
import breakpoint_generator

# blur spread infile outfile -fN | -pN -i [-sspread]
# Parameters

#     -fN extract formant envelope linear frequency-wise, using 1 point for every N equally-spaced frequency channels
#     -pN extract formant envelope linear pitch-wise, using N equally-spaced pitch bands per octave
#     -i quicksearch for formants (less accurate)
#     -sspread degree of spreading of spectrum (Range 0-1; Default is 1).
#         spread may vary over time 

def make_command():
    if random.random() < 0.5:
        # print("-f mode")
        parameter1 = "-f" + str(random.uniform(2,256))
        parameter_list = [parameter1]
        return Command("blur spread", 1, parameter_list)
    else:
        parameter1 = "-p" + str(random.uniform(1,12))
        # breakpoint parameter
        parameter2 = "-s"
        parameter_list = [parameter1, parameter2]
        return Command("blur spread", 2, parameter_list, BreakpointInfo(1, 0, 1))
    