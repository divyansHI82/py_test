# Write a python code to create menu based calculator.

def calculator():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Thanks for using the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue

        # Get numbers from the user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # Perform the selected operation
        if choice == '1':
            result = num1 + num2
            operation = "Addition"
        elif choice == '2':
            result = num1 - num2
            operation = "Subtraction"
        elif choice == '3':
            result = num1 * num2
            operation = "Multiplication"
        elif choice == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = num1 / num2
            operation = "Division"

        # Display result
        print(f"{operation} result: {result}")

# Run the calculator
calculator()

print("\nThis program is written and executed by Divyanshi Singhal (0221BCA150)\n")
