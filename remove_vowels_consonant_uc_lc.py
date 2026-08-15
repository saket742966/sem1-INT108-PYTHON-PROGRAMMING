# Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file.

vowels = 0
consonants = 0
uppercase = 0
lowercase = 0

with open("data.txt", "r") as file:
    for line in file:
        for char in line:

            if char.isalpha():
                if char.lower() in "aeiou":
                    vowels += 1
                else:
                    consonants += 1

                if char.isupper():
                    uppercase += 1
                elif char.islower():
                    lowercase += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

