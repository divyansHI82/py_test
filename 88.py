# Demonstrating Method Overloading and Method Overriding in Python

# Method Overloading Example (using default parameters)
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

# Method Overriding Example
class Animal:
    def sound(self):
        print("Animals make different sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Creating objects
calc = Calculator()
print("Method Overloading Example:")
print("Sum of 2 and 3:", calc.add(2, 3))
print("Sum of 1, 2 and 3:", calc.add(1, 2, 3))

print("\nMethod Overriding Example:")
animal = Animal()
dog = Dog()
animal.sound()
dog.sound()

print("\nThis program is written by Divyanshi Singhal ERP id is 0221BCA150.")
