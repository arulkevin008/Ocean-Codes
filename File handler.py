#File Handling
import os
f=open("myfile.txt","x")
print("File created")
with open("myfile.txt", "a") as f:
  f.write("Now the file has more content!\n")
  f.write("Python file handling!")
print("File written")
with open("myfile.txt") as f:
  print(f.read())
print("File readed")
os.remove("myfile.txt")
print("File deleted")