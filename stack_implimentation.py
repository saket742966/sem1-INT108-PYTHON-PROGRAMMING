# Write a python program to implement a stack using a list data structure

stack = []

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        element = input("Enter element: ")
        stack.append(element)
        print("Element pushed successfully.")

    elif choice == "2":
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            element = stack.pop()
            print("Popped element:", element)

    elif choice == "3":
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", stack[-1])

    elif choice == "4":
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Stack:", stack)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")