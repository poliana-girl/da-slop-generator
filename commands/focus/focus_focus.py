import random

from command import Command, BreakpointInfo
import breakpoint_generator

#  Usage
# focus focus inanalysisfile outanalysisfile -fN | -pN [-i] pk bw [-bbt] [-ttp] [-sval]

# Typical command line:
# focus focus raspdt.ana raspdtfoc.ana -f1 16 0.09 -b20 -t20000
# Parameters

#     -f extract formant envelope linear frequency-wise, using 1 point for every N equally-spaced frequency-channels
#     -p extract formant envelope linear pitchwise, using N equally-spaced pitch-bands per octave
#     -i quicksearch for formants (less accurate)
#     pk (maximum) number of peaks to find Range 1 – 16
#     bw bandwidth of peak-centred filters, in octaves
#     -bbt bottom frequency at which to start the search for peaks
#     -ttp top frequency at which to end the search for peaks
#     -sval the number of windows over which the peaks are averaged. This is an attempt to retain only peaks which are STABLE over time. Range: 2 – 4097. Default is 9.

#         bw (bandwidth), bt (bottom frequency) & tp (top frequency) may vary over time

def make_command():
    if random.random() < 0.5:
        # -f mode
        parameter1 = "-f" + str(random.uniform(1,12))
    else:
        # -p mode
        parameter1 = "-p" + str(random.uniform(1,12))

    parameter2 = random.uniform(1, 16)
    # breakpoint parameter
    parameter3 = "" # breakpoint_generator.breakpoint_generator(0.1, 10)
    parameter4 = "-s" + str(random.uniform(2,4097))
    
    parameter_list = [parameter1, parameter2, parameter3]
    return Command("focus focus", 3, parameter_list, BreakpointInfo(2, 0.1, 10))