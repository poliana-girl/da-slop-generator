import random

from command import Command

def make_command():
    parameter_list = [random.uniform(1,30000)]
    return Command("blur blur", 1, parameter_list)