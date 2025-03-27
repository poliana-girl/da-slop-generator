import random

from command import Command

#  Usage
# superaccu superaccu 1 inanalysisfile outanalysisfile [-ddecay] [-gglis] [-r]
# superaccu superaccu 2 inanalysisfile outanalysisfile [-ddecay] [-gglis] [-r]


# Example command line to sustain until louder data is present:

#     superaccu superaccu 3 rasp.ana raspsuperaccu.ana supaccutune.txt -d0.5 -g0.9
#     (supaccutune.txt: 60 63 67 70 73) (This example seemed to produce rather too much 'resonant tail' – the last 10 seconds were inaudible; the input file was 10 seconds long. So you may need to CUT some of the latter part of the output analysis file with SPEC CUT.) 

# Modes

#     1  Operates like FOCUS ACCU
#     2  Forces the (start of) resonances to the tempered scale

def make_command():
    mode = random.randint(1, 2)
    parameter1 = "-d" + str(random.uniform(0.01, 0.9))
    parameter2 = "-g" + str(random.uniform(-11.7, 11.7))
    parameter_list = [parameter1, parameter2]
    return Command("superaccu superaccu " + str(mode), 2, parameter_list)