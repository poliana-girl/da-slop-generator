# THIS ONE DOESN'T WORK ON MY MACHINE FOR SOME REASON!! like at all.. it just throws a memory error whenever you run it no matter what u do

import random

from command import Command

# selfsim selfsim inanalfile outanalfile self-similarity-index

# Example command line to expand the area of similar windows :

#     selfsim selfsim in.ana out.ana 2 

def make_command():
    parameter1 = 1
    parameter_list = [parameter1]
    return Command("selfsim selfsim", 1, parameter_list)