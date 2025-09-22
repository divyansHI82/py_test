# write a python code to check whether the string is palindrome or not.

def is_palindrome(s):
    
    s = s.replace(" ", " ").lower()
    return s == s[::-1]

string = input("Enter a String:")

if is_palindrome(string):
    print("The string is a palindrome.")
    
else:
    print("The string is not a palindrome.")
    
print("\nThis program is written and executed by Divyanshi Singhal (0221BCA150)\n")
