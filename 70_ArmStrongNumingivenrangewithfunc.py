# Write a python code to print all the armstrong number in a given range using function.

def is_armstrong(num):
    digits = str(num)                # Convert number to string to get digits
    power = len(digits)              # Number of digits
    total = 0

    for digit in digits:
        total += int(digit) ** power  # Add digit raised to the power of total digits

    return total == num              # Return True if Armstrong condition is met

# Function to print Armstrong numbers in a given range
def print_armstrong_numbers(start, end):
    print(f"\nArmstrong numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_armstrong(number):
            print(number)

# Taking input from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Calling the function
print_armstrong_numbers(start, end)

print("\nThis program is written and executed by Divyanshi Singhal (0221BCA150)\n")
