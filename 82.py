# Python program to demonstrate a custom (user-defined) module

# ---------- Custom Module ----------
def add(a, b):
    return a + b

def greet(name):
    return f"Hello {name}, welcome to Python!"

# Save this part as mymodule.py if running separately

# ---------- Using the Custom Module ----------
# Here we use the functions created above
print("Addition:", add(10, 20))
print(greet("Divyanshi"))


print("\nThis program is written by Divyanshi Singhal ERP id is 0221BCA150.")
