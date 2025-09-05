try:
    f = open("example.txt")
    print(f.read())
except:
    print("File not found!")
finally:
    print("Done")
print("This program is written by Divyanshi Singhal ERP I.D is 0221BCH150")