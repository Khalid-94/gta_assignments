while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print("Result:", x + y)
        case 2:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print("Result:", x - y)
        case 3:
            print("Exiting program...")
            break
        case _:
            print("Invalid choice")