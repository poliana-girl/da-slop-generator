import random

from command import Command
import breakpoint_generator

def make_command():
    parameter1 = "-i" + breakpoint_generator.breakpoint_generator(0, 1)
    parameter_list = [parameter1]
    return Command("combine cross", 1, parameter_list)