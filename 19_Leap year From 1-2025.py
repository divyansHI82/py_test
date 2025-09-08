count = 0
for year in range(1, 2026):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, end=" ")
        count += 1

print("\nTotal leap years:", count)
print("This program is written by Divyanshi Singhal ERP I.D is 0221BCH150")
