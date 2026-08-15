# Remove all the lines that contain the character “a” in a file and write it into another file.

with open("input.txt", "r") as file:
    with open("output.txt", "w") as new_file:

        for line in file:
            if "a" not in line:
                new_file.write(line)

