# Write a python code to print factorial of a given number using simple function (without recursion).

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# User input
num = int(input("Enter a number to find its factorial: "))
fact = factorial(num)

# Output
print(f"The factorial of {num} is: {fact}")

print("\nThis program is written and executed by Divyanshi Singhal (0221BCA150)\n")
