# Python program to demonstrate a decorator

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello, welcome to Python!")

# Calling the decorated function
greet()


print("\nThis program is written by Divyanshi Singhal ERP id is 0221BCA150.")
