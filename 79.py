# Python program to demonstrate decorator using functools.wraps

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def greet():
    """This function prints a greeting message."""
    print("Hello, everyone!")

# Calling the decorated function
greet()

# Checking if original metadata is preserved
print("Function Name:", greet.__name__)
print("Function Docstring:", greet.__doc__)

print("\nThis program is written by Divyanshi Singhal ERP id is 0221BCA150.")
