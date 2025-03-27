import random

from command import Command

#  Usage
# formants vocode infile infile2 outfile -fN | -pN [-llof] [-hhif] [-ggain]
# Parameters

#     -fN extract formant envelope linear frequency-wise, using 1 point for every N equally spaced frequency channels
#     -pN extract formant envelope linear pitchwise, using N equally-spaced pitch-bands per octave
#     -llof lof is low frquency, below which data is filtered out
#     -hhif hif is high frquency, above which data is filtered out
#     -ggain gain is the amplitude adjustment to the signal (normally < 1.0)


def make_command():
    if random.random() < 0.5:
        # print("-f mode")
        parameter1 = "-f" + str(random.uniform(2,256))
    else:
        # print("-p mode")
        parameter1 = "-p" + str(random.uniform(1,12))
        
    parameter_list = [parameter1]
    return Command("formants vocode", 1, parameter_list)