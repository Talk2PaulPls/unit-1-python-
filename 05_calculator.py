def calculator():
    print("Welcome to the Calculatinator-inator 9000!\n")
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Exponential")
    print("7. Remainder")
    choice = input("\nEnter choice: ")
    if choice == '1':
        result = first_number + second_number
        operation = "Addition"
    elif choice == '2':
        result = first_number - second_number
        operation = "Subtraction"
    elif choice == '3':
        result = first_number * second_number
        operation = "Multiplication"
    elif choice == '4':
        result = first_number / second_number
        operation = "Division"
    elif choice == '5':
        result = first_number // second_number
        operation = "Floor Division"
    elif choice == '6':
        result = first_number ** second_number
        operation = "Exponential"
    elif choice == '7':
        result = first_number % second_number
        operation = "Remainder"
    else:
        print("Invalid choice.")
        return
    print(f"\nResult of {operation}: {result}")
calculator()
