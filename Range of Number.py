# Prime, Perfect and Armstrong numbers in a range

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end+1):
    if num > 1 and all(num % i != 0 for i in range(2, num)):
        print(num, "Prime")
    if num == sum(i for i in range(1, num) if num % i == 0):
        print(num, "Perfect")
    if num == sum(int(d)**len(str(num)) for d in str(num)):
        print(num, "Armstrong")

print("This program is written by Divyanshi Singhal ERP I.D is 0221BCH150")