count = 0
print("Perfect numbers from 1 to 2025:")

for n in range(1, 2026):
    if n > 1 and sum(i for i in range(1, n) if n % i == 0) == n:
        print(n, end=" ")
        count += 1

print("\nTotal perfect numbers:", count)

print("This program is written by Divyanshi Singhal ERP I.D is 0221BCH150")
