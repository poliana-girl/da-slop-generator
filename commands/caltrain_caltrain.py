import random

from command import Command

def make_command():
    parameter1 = random.uniform(0.1,3)
    parameter2 = random.uniform(1, 3000)
    parameter_list = [parameter1, parameter2]
    return Command("caltrain caltrain", 2, parameter_list)