# Write a python code to print fibonaci series upto given input number using both approach using simple and recursion.

# -------- Iterative Method --------
def fibonacci_iterative(limit):
    a, b = 0, 1
    series = []
    while a <= limit:
        series.append(a)
        a, b = b, a + b
    return series

# -------- Recursive Method --------
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def generate_fibonacci_recursive(limit):
    series = []
    i = 0
    while True:
        fib = fibonacci_recursive(i)
        if fib > limit:
            break
        series.append(fib)
        i += 1
    return series

# -------- Main Program --------
# Take user input
num = int(input("Enter a number to generate Fibonacci series up to: "))

# Check for valid input
if num < 0:
    print("Please enter a non-negative number.")
else:
    print("\nFibonacci series using iterative method:")
    print(fibonacci_iterative(num))

    print("\nFibonacci series using recursive method:")
    print(generate_fibonacci_recursive(num))

print("\nThis program is written and executed by Divyanshi Singhal (0221BCA150)\n")
