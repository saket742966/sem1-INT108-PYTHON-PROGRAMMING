# Write a Program to check if the entered number is Armstrong or not.

print("\n" + "-" * 50)
print(" " * 17 + "Armstrong Number Checker")
print("-" * 50)

# take user input
while True:
    try:
        num = int(input("Enter a number : "))
        break
    except ValueError:
        print("Enter a valid number.")

# create list of digits
digits = []

for digit in str(num):
    digits.append(int(digit))

# count number of digits
digit_count = len(digits)

# find sum of digits raised to the power of digit count
sum_digits = 0
for i in digits:
    i = i ** digit_count
    sum_digits += i

# validate if armstrong or not
if sum_digits == num:
    print("Yes, ", num, "is an Armstrong Number")
else:
    print("No,", num, "is not an Armstrong Number")
    
    