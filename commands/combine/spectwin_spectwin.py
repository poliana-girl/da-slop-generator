import random

from command import Command


#  Usage
# spectwin spectwin 1-4 inanalfile1 inanalfile2 outanalfile [-ffrqint] [-eenvint] [-ddupl -sstep -rdec]

# Example command line to create combined spectra:

#     spectwin spectwin 1 in1.ana in2.ana out.ana 

# Modes

#     1  Formant envelope of inanalfile1 with the formant envelope of inanalfile2
#     2  Formant envelope of inanalfile1 with the total envelope of inanalfile2
#     3  Total envelope of inanalfile1 with the formant envelope of inanalfile2
#     4  Total envelope of inanalfile1 with the total envelope of inanalfile2

#         The formant envelope traces out the envelope formed by the peaks in the spectrum.
#         The total envelope traces out the envelope formed by EVERY channel in the spectrum. 

# Parameters

#     -ffrqint – dominance of the spectral frequencies of inanalfile2. (Range: 0 to 1. Default: 1.0)
#     -eenvint – dominance of the spectral envelope of inanalfile2. (Range: 0 to 1. Default: 1.0)

#     Note that the next three optional parameters are linked:
#     -ddupl – duplicate the sound of inanalfile1 dupl times, at higher pitches (Range: 0 to 8)
#     -sstep – the transposition step in (fractions of) semitones at each duplication (Range: 0 to 48)
#     -rdec – the amplitude level multiplier from one transposition to the next when creating the transposed duplications (Range: 0 to 1) 

def make_command():
    mode = random.randint(1, 4)
    parameter1 = "-f" + str(random.uniform(0, 1))
    parameter2 = "-e" + str(random.uniform(0, 1))
    parameter3 = "-d1"
    parameter4 = "-s" + str(random.uniform(0, 48))
    parameter5 = "-r" + str(random.uniform(0, 1))
    parameter_list = [parameter1, parameter2, parameter3, parameter4, parameter5]
    return Command("spectwin spectwin " + str(mode), 5, parameter_list)