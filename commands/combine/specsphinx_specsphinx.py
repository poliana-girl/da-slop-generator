import random

from command import Command



# Example command line to impose channel amplitudes:

#     specsphinx specsphinx 1 in1.ana in2.ana out.ana -b0.5 -f0.5 

# Modes

#     1  Impose channel amplitudes of inanalfile2 onto the channel frequencies of inanalfile1
#     2  Multiply the spectra 


    # -aampbalance – proportion of inanalfile1's amplitudes that are retained. Default = 0
    # -ffrqbalance – proportion of inanalfile2's frequencies injected into the output spectrum. Default = 0
    # -bbias – When non-zero, it adds a proportion of the original files to the output:
    #    < 1: add inanalfile1 to outanalfile in the proportion determined by the formula -bias/(1 + bias)
    #    > 1: add inanalfile2 to outanalfile in the proportion determined by the formula bias/(1 - bias)
    # -ggain – overall gain applied to the output

    #     ampbalance, frqbalance, bias and gain may vary over time 

#  Usage
# specsphinx specsphinx 1 inanalfile1 inanalfile2 outanalfile [-aampbalance] [-ffrqbalance]
# OR:
# specsphinx specsphinx 2 inanalfile1 inanalfile2 outanalfile [-bbias] [-ggain]


def make_command():
    mode = random.randint(1, 2)
    if mode == 1:
        parameter1 = "-a" + str(random.uniform(0, 1))
        parameter2 = "-f" + str(random.uniform(0, 1))
        parameter_list = [parameter1, parameter2]
        return Command("specsphinx specsphinx " + str(mode), 2, parameter_list)
    elif mode == 2:
        parameter1 = "-b" + str(random.uniform(-1, 1))
        parameter_list = [parameter1]
        return Command("specsphinx specsphinx " + str(mode), 1, parameter_list)