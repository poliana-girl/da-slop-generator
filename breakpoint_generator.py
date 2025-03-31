import random
import os

from date_time_format import get_formatted_date_time

breakpoint_directory_name = "breakpoints"

def breakpoint_generator(low_bound, high_bound, sound_length):

    current_time = get_formatted_date_time()
    filename = "breakpoint_" + current_time + ".brk"

    if not os.path.exists(breakpoint_directory_name):
        os.mkdir(breakpoint_directory_name)
    
    filename = breakpoint_directory_name + "/breakpoint_" + str(random.randint(10000000, 99999999)) + ".brk"

    file = open(filename, "x")
    
    # time = 0
    # for i in range(20):
    #     time = time + random.randint(1, 60)
    #     value = random.uniform(low_bound, high_bound)
    #     file.write(str(time))
    #     file.write(" ")
    #     file.write(str(value))
    #     file.write("\n")
    
    number_of_values = random.randint(1, 100)

    # generate number_of values # of random times inside range of the sound's length
    times = []
    for i in range(number_of_values):
        time = random.uniform(0, sound_length)
        times.append(time)

    times.sort()

    for i in range(number_of_values):
        time = 0 
        value = random.uniform(low_bound, high_bound)
        file.write(str(times[i]))
        file.write(" ")
        file.write(str(value))
        file.write("\n")

    file.close()
    return filename
