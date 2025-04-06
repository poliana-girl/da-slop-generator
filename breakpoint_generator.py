import random
import os

from utilities import get_formatted_date_time

breakpoint_directory_name = "breakpoints"

# change to small values to up the chaos
breakpoint_chaos_multiplier = 0.1

def breakpoint_generator(low_bound, high_bound):

    current_time = get_formatted_date_time()
    filename = "breakpoint_" + current_time + ".brk"

    if not os.path.exists(breakpoint_directory_name):
        os.mkdir(breakpoint_directory_name)
    
    filename = breakpoint_directory_name + "/breakpoint_" + str(random.randint(10000000, 99999999)) + ".brk"

    file = open(filename, "x")
    
    time = 0
    for i in range(int(20 * (1/breakpoint_chaos_multiplier))):
        time = time + random.uniform(1*breakpoint_chaos_multiplier, 60*breakpoint_chaos_multiplier)
        value = random.uniform(low_bound, high_bound)
        file.write(str(time))
        file.write(" ")
        file.write(str(value))
        file.write("\n")
    
    file.close()
    return filename
