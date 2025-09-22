# Write a python code to print factorial of a given number using recursive function.

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n - 1)
    return n * factorial(n - 1)

# Ask the user to enter a number
num = int(input("Enter a number to find its factorial: "))

# Handle negative input
if num < 0:
    print("Sorry, factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}.")

print("\nThis program is written and executed by Divyanshi Singhal (0221BCA150)\n")
