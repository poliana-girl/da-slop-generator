import random

from command import Command


#  Usage
# combine mean mode infile infile2 outfile [-llofrq] [-hhifrq] [-cchans] [-z]
# Modes

#     1  mean channel amp of 2 files : mean of two pitches
#     2  mean channel amp of 2 files : mean of two frequencies
#     3  channel amp from file 1     : mean of two pitches
#     4  channel amp from file 1     : mean of two frequencies
#     5  channel amp from file 2     : mean of two pitches
#     6  channel amp from file 2     : mean of two frequencies
#     7  max channel amp of 2 files : mean of two pitches
#     8  max channel amp of 2 files : mean of two frequencies

# Parameters

#     infile, infile2 – input analysis files made with PVOC
#     outfile – output analysis file
#     -llofrq – low frequency limit of channels to look at
#     -hhifrq – high frequency limit of channels to look at
#     -cchans– number of significant channels to compare. Default: ALL within range.

def make_command():
    mode = random.randint(1, 8)
    parameter_list = []
    return Command("combine mean " + str(mode), 0, parameter_list)