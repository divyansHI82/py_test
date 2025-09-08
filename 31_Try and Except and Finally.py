try:
  file=open('example.txt','r')
  content = file.read()
except FileNotFoundError:
      print("Error.the file was not found.")
finally:
      file.close()
      print("This program is written by Divyanshi Singhal ERP ID is 0221BCA150")
