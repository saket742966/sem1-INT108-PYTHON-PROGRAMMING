# Read a text file line by line and display each word separated by a #

with open("data.txt", "r") as file:

    for line in file:
        words = line.split()
        print("#".join(words))