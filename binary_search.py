# Create a binary file with name and roll no. Search for a given roll number and display the name, if not found display appropriate message.

import pickle

# Create binary file
with open("students.dat", "wb") as file:

    while True:
        name = input("Enter student name: ")
        roll_no = int(input("Enter roll number: "))

        student = {
            "name": name,
            "roll_no": roll_no
        }

        pickle.dump(student, file)

        choice = input("Do you want to add another student? (y/n): ")

        if choice.lower() != "y":
            break


# Search for roll number
search_roll = int(input("\nEnter roll number to search: "))

found = False

with open("students.dat", "rb") as file:

    try:
        while True:
            student = pickle.load(file)

            if student["roll_no"] == search_roll:
                print("Name:", student["name"])
                found = True
                break

    except EOFError:
        pass

if not found:
    print("Roll number not found.")

