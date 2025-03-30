import random
import os

from date_time_format import get_formatted_date_time

breakpoint_directory_name = "breakpoints"

def breakpoint_generator(low_bound, high_bound):

    current_time = get_formatted_date_time()
    filename = "breakpoint_" + current_time + ".brk"

    if not os.path.exists(breakpoint_directory_name):
        os.mkdir(breakpoint_directory_name)
    
    filename = breakpoint_directory_name + "/breakpoint_" + str(random.randint(10000000, 99999999)) + ".brk"

    file = open(filename, "x")
    
    time = 0
    for i in range(20):
        time = time + random.randint(1, 60)
        value = random.uniform(low_bound, high_bound)
        file.write(str(time))
        file.write(" ")
        file.write(str(value))
        file.write("\n")
    
    file.close()
    return filename
