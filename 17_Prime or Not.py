# Check prime number

num = int(input("Enter a number: "))

if num > 1 and all(num % i != 0 for i in range(2, num)):
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")

print("This program is written by Divyanshi Singhal ERP I.D is 0221BCH150")
