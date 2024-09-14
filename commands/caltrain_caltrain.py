import random

from command import Command

def make_command():
    parameter_list = [random.uniform(0.1,3), random.uniform(1, 3000)]
    return Command("caltrain caltrain", 2, parameter_list)