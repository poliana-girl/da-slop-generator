import random
import datetime

def breakpoint_generator(low_bound, high_bound):
    filename = "breakpoint_" + datetime.datetime.now().strftime("%I:%M:%S%p") + ".brk"
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
