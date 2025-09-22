# write a python code to calculate the length of a string without using built-in len() function.

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

# Example usage
text = "Hello, world!"
length = string_length(text)
print(f"The length of the string is: {length}")

print("\nThis program is written and executed by Divyanshi Singhal (0221BCA150)\n")
