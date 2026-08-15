# Write a Program to enter the string and to check if it’s palindrome or not using loop.

print("\n" + "-" * 50)
print(" " * 17 + "Palindrome checker")
print("-" * 50)

# take user input and validate
while True :
    text = input("Enter a word : ")
    if text.strip() == "" :
        print("Please enter a word.")
        continue
    break

# reverse the text
reverse_text = text[::-1]

# equate and check if palindrome
if text == reverse_text :
    print("Yes, ",text, "is palindrome")
else:
    print("No, ", text,"is not palindrome")


