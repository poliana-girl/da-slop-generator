import random
import datetime
import os

breakpoint_directory_name = "breakpoints"

def breakpoint_generator(low_bound, high_bound):
    if not os.path.exists(breakpoint_directory_name):
        os.mkdir(breakpoint_directory_name)
    
    filename = breakpoint_directory_name + "/breakpoint_" + datetime.datetime.now().strftime("%I:%M:%S%p") + ".brk"
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
