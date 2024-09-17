# this one works fine most of the time but sometimes it'll crash because of the error below:
# ERROR: Attack time on 1st source is at or beyond end of 2nd.

import random

from command import Command
import breakpoint_generator

# specross partials inanalfile1 inanalfile2 outanalfile tuning minwin signois harmcnt lo hi thresh level interp

#  Example command line to interpolate pitched partials between analysis files:

#     specross partials p3c.ana horn2.ana p3xh2.ana 4 5 80 5 50 2000 0.2 1 0.2 

# Parameters

#     tuning – the range in semitones within which the harmonics are 'in tune'; higher values are more 'forgiving' and use more of the second file (Range: 0.0 to 6.0, Default: 1)
#     minwin – the minimum number of adjacent windows that must be pitched, for a pitch-value to be registered (Default: 2)
#     signois – the signal-to-noise ration, in decibels (Default 80dB). Windows that are greater than signoisdB below the maximum level in the sound are assumed to be noise, and any detected pitch is assumed to be spurious.
#     harmcnt – The number of the 8 loudest peaks in the spectrum which much be harmonics in order to confirm that the sound is pitched (Default 5)
#     lo – the lowest acceptable frequency for a pitch (Default: 10Hz)
#     hi – the highest acceptable frequency for a valid pitch (Default: Nyquist/8, i.e., 2756.25 at a sample rate of 44100: sample rate divided by 2 and then divided by 8: 44100 ÷ 2 = 22050 ÷ 8 = 2756.25. The program adjusts hi according to the sample rate of the input file.)
#     thresh – the minimum acceptable level of any partial found, if it is to be used in reconstructed spectrum (level relative to loudest partial). A lower value is more 'forgiving' and uses more of the second file. A higher value accepts only the loudest partials.
#     level – the level of the output (Default: 1.0). Use if reapplying inanalfile1 to several inanalfile2s, whose relative level is important.
#     interp – the interpolation between inanalfile2 and inanalfile1, which can vary through time. Breakpoint time values will be scaled to the duration if inanalfile1. A lower value reduces the effect of inanalfile2, i.e., it 'lets through' more of a recognisable second file, rather than just its partials. (Default? Range?)
#     -a – retain the loudness contour of inanalfile2, under the contour of inanalfile1. What does this mean?
#     -p – extend the first stable pitch of inanalfile1 to the start of the outanalfile 

def make_command():
    # tuning – the range in semitones within which the harmonics are 'in tune'; higher values are more 'forgiving' and use more of the second file (Range: 0.0 to 6.0, Default: 1)
    parameter1 = random.uniform(3, 6)

    # minwin – the minimum number of adjacent windows that must be pitched, for a pitch-value to be registered (Default: 2)
    parameter2 = 2 # random.uniform(2, 10)

    # signois – the signal-to-noise ration, in decibels (Default 80dB). Windows that are greater than signoisdB below the maximum level in the sound are assumed to be noise, and any detected pitch is assumed to be spurious.
    parameter3 = random.uniform(20, 40)

    # harmcnt – The number of the 8 loudest peaks in the spectrum which much be harmonics in order to confirm that the sound is pitched (Default 5)
    parameter4 = 1

    # lo – the lowest acceptable frequency for a pitch (Default: 10Hz)
    parameter5 = 10

    # hi – the highest acceptable frequency for a valid pitch (Default: Nyquist/8, i.e., 2756.25 at a sample rate of 44100: sample rate divided by 2 and then divided by 8: 44100 ÷ 2 = 22050 ÷ 8 = 2756.25. The program adjusts hi according to the sample rate of the input file.)
    parameter6 = 3000

    # thresh – the minimum acceptable level of any partial found, if it is to be used in reconstructed spectrum (level relative to loudest partial). A lower value is more 'forgiving' and uses more of the second file. A higher value accepts only the loudest partials.
    parameter7 = 0.1

    # level – the level of the output (Default: 1.0). Use if reapplying inanalfile1 to several inanalfile2s, whose relative level is important.
    parameter8 = 1

    # interp – the interpolation between inanalfile2 and inanalfile1, which can vary through time. Breakpoint time values will be scaled to the duration if inanalfile1. A lower value reduces the effect of inanalfile2, i.e., it 'lets through' more of a recognisable second file, rather than just its partials. (Default? Range?)
    parameter9 = 1

    parameter_list = [parameter1, parameter2, parameter3, parameter4, parameter5, parameter6, parameter7, parameter8, parameter9]
    return Command("specross partials", 9, parameter_list)