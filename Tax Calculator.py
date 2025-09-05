income = int(input())
tax = 0

if income > 3000000:
    tax += (income - 3000000) * 0.4
    income = 3000000
if income > 2000000:
    tax += (income - 2000000) * 0.3
    income = 2000000
if income > 1000000:
    tax += (income - 1000000) * 0.2
    income = 1000000
if income > 500000:
    tax += (income - 500000) * 0.1
    income = 500000
if income > 250000:
    tax += (income - 250000) * 0.05

print(tax)

print("This program is written by Divyanshi Singhal ERP I.D is 0221BCH150")