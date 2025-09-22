# Write a python code to calculate factorial of a given number.

def factorial(n):
    # Factorial is only defined for non-negative integers
    if n < 0:
        return "Sorry, factorial is not defined for negative numbers."

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Ask the user to enter a number
num = int(input("Enter a number to find its factorial: "))

# Show the result
print(f"The factorial of {num} is {factorial(num)}.")

print("\nThis program is written and executed by Divyanshi Singhal (0221BCA150)\n")
