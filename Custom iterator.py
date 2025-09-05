def my_iter(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in my_iter(5):
    print(num)
print("This program is written by Divyanshi Singhal ERP I.D is 0221BCH150")