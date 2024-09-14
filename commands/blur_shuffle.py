import random

from command import Command

#  Usage
# blur shuffle infile outfile domain-image grpsize
# Parameters

#     infile – input analysis file made with PVOC
#     outfile – output analysis file
#     domain-image – this consists of two strings of letters, separated by a hyphen ('-'); the first string is the domain and the second string is the image, e.g., 'abc-abbabcc'.

#         The domain letters represent a group of consecutive infile analysis windows, e.g., 'abcd'.
#         The image is any permutation of, or selection from, these domain letters ­ these letters may be omitted or repeated in the image string, e.g., 'aaaaaaaadaaa'. 

#     grpsize – the number of analysis windows corresponding to each letter of domain.

#         Each letter then represents a group of grpsize windows and the whole group is treated as one unit in the shuffling process. 



def make_command():
    letters = ["a", "b", "c", "d", "e", "f", "g"]
    image = ""
    for i in range(random.randint(10, 30)):
        image = random.choice(letters) + image
    print(image)
    parameter1 = "abcdefg-" + image
    parameter2 = random.uniform(5, 300)
    parameter_list = [parameter1, parameter2]
    return Command("blur shuffle", 2, parameter_list)