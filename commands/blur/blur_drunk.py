import random

from command import Command

# blur drunk infile outfile range starttime duration [-z]

#     infile – input analysis file made with PVOC
#     outfile – output analysis file
#     range –the maximum step (in windows) for the drunken walk: <= 64
#     starttime– the time (in seconds) in the file at which the walk should begin
#     duration– the required duration of the outfile after re-synthesis ­ it may be longer than infile
#     -z eliminates zero steps (window-repeats) in the drunken walk

def make_command():
    parameter1 = random.uniform(1, 64)
    parameter2 = 0
    parameter3 = random.uniform(30,500)
    parameter_list = [parameter1, parameter2, parameter3]
    return Command("blur drunk", 3, parameter_list)