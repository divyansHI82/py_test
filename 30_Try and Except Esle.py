try:
    number=int(input("Enter a number:"))
    result=10/number
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print("The result is {result}.")
print("This program is written by Divyanshi Singhal ERP ID is 0221BCA150")
