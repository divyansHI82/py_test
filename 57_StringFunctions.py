# Write a python code to demonstrate string function.

text = " Hello World! "

# Changing Case

lowercase_text = text.lower()
print(lowercase_text)
uppercase_text = text.upper()
print(uppercase_text)
title_text = text.title()
print(title_text)

# Trimming Whitespace

stripped_text = text.strip()
print(stripped_text)
left_stripped_text = text.lstrip()
print(left_stripped_text)
right_stripped_text = text.rstrip()
print(right_stripped_text)

# Splitting and Joining 

words = stripped_text.split(",")
print(words)
joined_text = "-".join(words)
print(joined_text)

# Replacing and Finding 

replaced_text = stripped_text.replace("World", "Python")
print(replaced_text)
index = stripped_text.find("World")
print(index)
count = stripped_text.count("o")
print(count)

print("\nThis program is written and executed by Divyanshi Singhal (0221BCA150)\n")
