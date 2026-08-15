# Read a file line by line and print it.

file = open("data.txt", "r")

for line in file:
    print(line, end="")

file.close()
