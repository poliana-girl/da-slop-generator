# this one clips really badly, so badly that the entire signal becomes inaudible (and weirdly enough, only in one channel most of the time)
# it's really powerful though and the effect is pretty cool so i'd like to figure out how to get it to work

import random

from command import Command
import breakpoint_generator

# hilite arpeg 1-4 infile outfile wave rate [-pU] [-lX] [-hY] [-bZ] [-aA] [-Nk] [-sS] [-T] [-K]
# hilite arpeg 5-8 infile outfile wave rate [-pU] [-lX] [-hY] [-bZ] [-aA]
# Modes

#     1  ON...................Play components inside arpeggiated band ONLY
#     2  BOOST...........Amplify snds in band. Others play unamplified
#     3  BELOW_BOOST.....INITIALLY play components in & below band ONLY

#         THEN amplify sounds in band. Others play unamplified
#         (NOT with downramp – illogical)

#     4  ABOVE_BOOST.....INITIALLY play components in & above band ONLY

#         THEN amplify sounds in band. Others play unamplified
#         (NOT with upramp – illogical: with sin/saw startphase > 0.5)

#     5  BELOW...........Play components in & below arpeggiated band ONLY
#     6  ABOVE...........Play components in & above arpeggiated band ONLY
#     7  ONCE_BELOW......INITIALLY Play components in and below band ONLY

#         THEN play whole sound as normal. (NOT with downramp – illogical)

#     8  ONCE_ABOVE......INITIALLY Play components in and above arpeggiated band ONLY

#         THEN play whole sound as normal
#         (NOT with upramp – illogical: with sin/saw startphase > 0.5)

# Parameters


#     wave – 1 = downramp : 2 = sin : 3 = saw : 4 = upramp
#     rate – number of sweeps per second (can be < 1)
#     -pU – start_phase: range 0-1 (limited range for some cases); may not affect the sound very much
#     -lX – lowest frequency arpeg sweeps down to; Default = 0
#     -hY – highest frequency arpeg sweeps up to; Default nyquist
#     -bZ – bandwidth of sweep band (in Hz); Default = nyquist/channel_cnt (i.e., sample rate/2/channel count)
#     -aA – amplification of arpegtones; Default = 10.0
#     -Nk – nonlinear decay arpegtones; > 1 faster, < 1 slower; must be > 0 (range: 0.02 to 50 – take care with values higher than about 5, as can reduce output to silence)
#     -sS – number of windows over which arpegtones sustained: Default = 3 (high values, esp. with a long decay time, can cause amplitude overflow)
#     -T – In sustains, TRACK changing frquency of source (Default = retain start frquency)
#     -K – Let sustains run to zero before new arpegtone attack is accepted
#     (Default: re-attack once sustains fall below current input level)

#     All parameters may vary over time, except for wavetype and startphase


def make_command():
    mode = 2 # random.randint(1, 8)
    
    parameter1 = 2
    parameter2 = breakpoint_generator.breakpoint_generator(0.1, 3)

    # [-lX] [-hY] [-bZ] [-aA]    

#     -lX – lowest frequency arpeg sweeps down to; Default = 0
    parameter3 = "-l" + breakpoint_generator.breakpoint_generator(0, 12000)
#     -hY – highest frequency arpeg sweeps up to; Default nyquist
    parameter4 = "-h" + breakpoint_generator.breakpoint_generator(12000, 24000)
#     -bZ – bandwidth of sweep band (in Hz); Default = nyquist/channel_cnt (i.e., sample rate/2/channel count)
    parameter5 = "-b" + breakpoint_generator.breakpoint_generator(50, 24000)
#     -aA – amplification of arpegtones; Default = 10.0
    parameter6 = "-a" + "2" # breakpoint_generator.breakpoint_generator(1, 10)
    
    
    parameter_list = [parameter1, parameter2, parameter3, parameter4, parameter5, parameter6]
    return Command("hilite arpeg " + str(mode), 6, parameter_list)