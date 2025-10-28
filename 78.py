# Python program to demonstrate decorator with arguments

def multiply_decorator(n):
    def decorator(func):
        def wrapper(x):
            result = func(x)
            return result * n
        return wrapper
    return decorator

@multiply_decorator(5)  # Passing argument to decorator
def number(x):
    return x

print("Result:", number(10))


print("\nThis program is written by Divyanshi Singhal ERP id is 0221BCA150.")
