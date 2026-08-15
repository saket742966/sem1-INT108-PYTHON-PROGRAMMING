# Recursively find the factorial of a natural number.

print("\n" + "-" * 50)
print(" " * 15 + "Factorial Calculator")
print("-" * 50)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


while True:
    try:
        num = int(input("Enter a natural number: "))

        if num <= 0:
            print("Please enter a natural number.")
            continue

        break

    except ValueError:
        print("Enter a valid number.")

result = factorial(num)

print("Factorial of", num, "is", result)
