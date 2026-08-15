# Write a program to find whether an inputted number is perfect or not.

print("\n" + "-" * 50)
print(" "* 17 + "Perfect Number Checker")
print("-" * 50)
global num
while True :
    try :
        num = int(input("Enter a number to check : "))
        break
    except ValueError:
        print("Enter a valid number.")

sum_divisors = 0

for i in range(1 , num) :
    if num % i == 0:
        sum_divisors += i
        
if sum_divisors == num :
    print(num, "is a perfect number !!")
    
else :
    print("Opps !", num, "is not a perfect number.")
        