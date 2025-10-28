# Defining a class, creating objects, and accessing properties inside methods

class Student:
    def __init__(self, name, erp_id):
        self.name = name
        self.erp_id = erp_id

    def display(self):
        print("Student Name:", self.name)
        print("ERP ID:", self.erp_id)

# Creating objects
s1 = Student("Divyanshi Singhal", "0221BCA150")
s2 = Student("Aarav Sharma", "0221BCA120")

# Accessing properties using method
s1.display()
print()
s2.display()

print("\nThis program is written by Divyanshi Singhal ERP id is 0221BCA150.")
