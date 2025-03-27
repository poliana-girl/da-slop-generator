import random

from command import Command

# blur chorus 1 infile outfile aspread
# blur chorus 2-4 infile outfile fspread
# blur chorus 5-7 infile outfile aspread fspread

# aspread – maximum random scatter of partial-amps (Range 1-1028)
# fspread – maximum random scatter of partial-frqs (Range 1-4)

def make_command():
    mode = random.randint(1, 7)
    parameter_list = []
    
    if mode == 1:
        parameter1 = random.uniform(1,1028)
        parameter_list = [parameter1]
        return Command("blur chorus 1", 1, parameter_list)

    elif mode >= 2 and mode <= 4:
        parameter1 = random.uniform(1,4)
        parameter_list = [parameter1]
        return Command("blur chorus " + str(mode), 1, parameter_list)

    elif mode >= 5 and mode <= 7:
        parameter1 = random.uniform(1,1028)
        parameter2 = random.uniform(1,4)
        parameter_list = [parameter1, parameter2]
        return Command("blur chorus " + str(mode), 2, parameter_list)
    
    