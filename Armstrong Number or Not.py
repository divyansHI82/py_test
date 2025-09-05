
# Check Armstrong number

num = int(input("Enter a number: "))
n = len(str(num))

if num == sum(int(digit) ** n for digit in str(num)):
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")

print("This program is written by Divyanshi Singhal ERP I.D is 0221BCH150")