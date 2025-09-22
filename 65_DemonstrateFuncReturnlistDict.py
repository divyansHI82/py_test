# Write a python code to demonstrate a Function which returns list/Dictionary.

def get_squares(numbers):
    squares = [n ** 2 for n in numbers]
    return squares

nums = [1,2,3,4]
squares_list = get_squares(nums)
print(squares_list)

print("\nThis program is written and executed by Divyanshi Singhal (0221BCA150)\n")
