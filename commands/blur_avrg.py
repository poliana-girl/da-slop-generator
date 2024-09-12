import random

from command import Command

def make_command():
    parameter_list = [random.uniform(2,513)]
    return Command("blur avrg", 1, parameter_list)