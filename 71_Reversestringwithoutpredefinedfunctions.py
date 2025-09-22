# write a python code to reverse a string without using predefined functions.

def reverse_string(s):
    reversed_str = ""
    index = len(s) - 1  # Start from the last character
    
    while index >= 0:
        reversed_str += s[index]
        index -= 1
        
    return reversed_str

# Example usage:
input_str = "hello"
print("Original string:", input_str)
print("Reversed string:", reverse_string(input_str))

print("\nThis program is written and executed by Divyanshi Singhal (0221BCA150)\n")
