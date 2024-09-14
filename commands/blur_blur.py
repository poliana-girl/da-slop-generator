import random

from command import Command

def make_command():
    parameter1 = random.uniform(1,30000)
    parameter_list = [parameter1]
    return Command("blur blur", 1, parameter_list)