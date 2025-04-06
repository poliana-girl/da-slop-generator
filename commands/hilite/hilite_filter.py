import random

from command import Command
import breakpoint_generator

#  Usage
# hilite filter  1–4    infile outfile frq1 Q
# hilite filter  5–6    infile outfile frq1 Q gain
# hilite filter  7–10  infile outfile frq1 frq2 Q
# hilite filter 11–12 infile outfile frq1 frq2 Q gain
# Modes

#      1   high pass filter
#      2   high pass filter (normalised output)
#      3   low pass filter
#      4   low filter (normalised output)
#      5   high pass filter with gain
#      6   low pass filter with gain
#      7   band pass filter
#      8   band pass filter (normalised output)
#      9   notch filter
#     10  notch filter (normalised output)
#     11  band pass filter with gain
#     12  notch filter with gain

# Parameters

#     infile – input analysis file made with PVOC
#     outfile – output analysis file
#     frq1 – filter cutoff frequency
#     frq1 with frq2 – limits of filter band
#     Q – width of filter skirts, in Hz (Range: > 0)

#         Here one is entering filter bandwidth directly. The smaller the Hz value for Q (i.e., the filter's bandwidth), the narrower the pitch focus of the filter.

#     gain – amplification of the resulting sound

#         frq1, frq2 and Q may vary over time

def make_command():
    mode = random.choice([2, 4, 8, 10])

    if mode == 2 or mode == 4:
        # frq1
        parameter1 = breakpoint_generator.breakpoint_generator(10, 24000)
        # Q
        parameter2 = breakpoint_generator.breakpoint_generator(1, 500)
        parameter_list = [parameter1, parameter2]
        return Command("hilite filter " + str(mode), 2, parameter_list)
    elif mode == 8 or mode == 10:
        # frq1
        parameter1 = breakpoint_generator.breakpoint_generator(10, 24000)
        # frq2
        parameter2 = breakpoint_generator.breakpoint_generator(10, 24000)
        # Q
        parameter3 = breakpoint_generator.breakpoint_generator(1, 500)
        parameter_list = [parameter1, parameter2, parameter3]
        return Command("hilite filter " + str(mode), 3, parameter_list)
    