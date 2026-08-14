# // Program to enter two numbers and print the arithmetic operations like +,-,*, /, // and %.

while True :
    try:
        a = int(input("Enter first number : "))
        break
    except ValueError:
        print("Enter a valid number.")
        
while True :
    try:
        b = int(input("Enter second number : "))
        break
    except:
        print("Enter a valid number.")

def main_menu():
    print("\n" + "*** Which operation do you want to perform ?***")
    print()
    
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulous Division")
    print("7. All of the above")
    
    while True :
        try :
            choice = int(input("Enter your choice from 1-7 : "))
            if choice < 1 or choice > 7 :
                print("Enter a valid choice from 1 to 7 !")
                continue
            break
        except ValueError:
            print("Enter a valid choice from 1 to 7")
    
    if choice == 1 :
        addition()
    
    elif choice == 2 :
        substraction()
    
    elif choice == 3 :
        multiplication()
        
    elif choice == 4 :
        division()
        
    elif choice == 5 :
        floor_divison()
        
    elif choice == 6 :
        modulous()

    elif choice == 7 :
        all_operation()


def addition():
    add = a + b
    print("Sum of", a, "and", b, "is", add)

def substraction():
    sub = a - b
    print("Difference of", a, "and", b, "is", sub)

def multiplication():
    mul = a * b
    print("Product of", a, "and", b, "is", mul)

def division():
    div = a / b
    print("Division of", a, "and", b, "is", div)

def floor_divison():
    flo = a // b
    print("Floor Division of", a, "and", b, "is", flo)

def modulous():
    mod = a % b
    print("Modulous of", a, "and", b, "is", mod)
    
def all_operation():
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    flo = a // b
    mod = a % b
    print("Sum of", a, "and", b, "is", add)
    print("Difference of", a, "and", b, "is", sub)
    print("Product of", a, "and", b, "is", mul)
    print("Division of", a, "and", b, "is", div)
    print("Floor Division of", a, "and", b, "is", flo)
    print("Modulous of", a, "and", b, "is", mod)
    

main_menu()
    
