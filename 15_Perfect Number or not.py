# Check perfect number

num = int(input("Enter a number: "))

if num == sum(i for i in range(1, num) if num % i == 0):
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")

print("This program is written by Divyanshi Singhal ERP I.D is 0221BCH150")
