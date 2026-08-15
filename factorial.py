# Write a Program to find factorial of the entered number.

print("\n" + "-" * 50)
print(" " * 17 + "Factorial Calculator")
print("-" * 50)

# take user input
while True:
    try:
        num = int(input("Enter a number : "))
        break
    except ValueError:
        print("Enter a valid number.")

factorial = 1
for i in range(num, 0, -1):
    factorial *= i

print()
print("Factorial of", num, "is", factorial)