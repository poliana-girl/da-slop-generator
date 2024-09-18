import random

from command import Command

#  Usage
# glisten glisten inanalfile outanalfile grpdiv setdur [-ppitchshift] [-ddurrand] [-vdivrand]

# Example command line to enliven an otherwise fairly static spectrum:

#     glisten glisten in.ana out.ana 4 250 -p3 -d0.7 -v0.25 

# Parameters


#     grpdiv – the number of sets into which to divide the analysis-channels. For example, when grpdiv = 4, the program will process the partitions and channels randomly among 4 sets with the total number of channels ÷ 4 per set. Note that grpdiv must be an exact divisor of the channel count. (Range: 2 to channel-count)
#     setdur – the number of windows for which a set-of-channels persists before we switch to the next set-of-chans. (Range: 1 to 1024)
#     -ppitchshift – The maximum range in (possibly fractional) semitones of random plus or minus pitch shifting (i.e., upwards or downwards) of each channel set. (Range: 0.0 to 12.0. Default: 0.0)
#     -ddurrand – the randomisation of setdur between 1 and setdur. (Range: 0 to 1)
#     -vdivrand – randomise the number of channels in each set in a group. (Range: 0 to 1.)
#     In the normal case, each set-of-channels has an equal number of channels. When divrand is > 0, a group will have sets of different sizes. 


def make_command():
    parameter1 = random.choice([2, 4, 8, 16, 32, 64])
    parameter2 = random.uniform(1, 1024)
    parameter3 = "-p" + str(random.uniform(0, 12))
    parameter4 = "-d" + str(random.uniform(0, 1))
    parameter5 = "-v" + str(random.uniform(0, 1))
    parameter_list = [parameter1, parameter2, parameter3, parameter4, parameter5]
    return Command("glisten glisten", 5, parameter_list)