# Write a Program to enter the number of terms and to print the Fibonacci Series.

print("\n" + "-" * 50)
print(" " * 17 + "Fibonacci Series")
print("-" * 50)

# take "terms" input from user
while True:
    try:
        terms = int(input("Enter number of terms: "))

        if terms <= 0:
            print("Enter a positive number.")
            continue

        break

    except ValueError:
        print("Enter a valid number.")
 
# inital first two terms
a = 0
b = 1

# looping and changing the values for getting desired number of terms
for i in range(terms):
    print(a, end=" ")

    next_num = a + b
    a = b
    b = next_num

        
