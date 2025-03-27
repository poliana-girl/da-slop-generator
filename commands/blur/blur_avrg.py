import random

from command import Command

def make_command():
    parameter1 = random.uniform(2,513)
    parameter_list = [parameter1]
    return Command("blur avrg", 1, parameter_list)