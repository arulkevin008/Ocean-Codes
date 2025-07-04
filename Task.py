#Even List
# def Even_List():
#     List=list(map(int,input("Enter the Elements for the List:").split()))
#     Even_List=[]
#     for i in List:
#         if i%2==0:
#             Even_List.append(i)
#     print(Even_List)
# Even_List()

#File Handling
# names = []
# for i in range(3):
#     name = input("Enter name: ")
#     names.append(name)
# with open("names.txt", "w") as file:
#     for name in names:
#         file.write(name + "\n")
# print("\nNames in the file:")
# with open("names.txt", "r") as file:
#     for line in file:
#         print(line.strip())

#Exeption
# try:
#     a,b=map(int,input("Enter two no:").split())
#     print(a//b)
# except ZeroDivisionError as e:
#     print("Error:",e)
# except ValueError as e:
#     print("Error:",e)

#Rectangle
# class Rectangle:
#     def area(self):z
#         L,B=map(int,input().split())
#         print("Area of the Rectangle:",L*B)
# A=Rectangle()
# A.area()

#Dictionary
names = []
mark = []
avg = []
for i in range(3):
    name = input("Enter the name for student: ")
    marks = list(map(int, input("Enter 3 marks separated by spaces: ").split()))
    names.append(name)
    mark.append(marks)
for value in mark:
    Sum=0
    Sum=sum(value)
    average = Sum // len(value)  
    avg.append(average)
print("Student Marks:", dict(zip(names, mark)))
print("Student Averages:", dict(zip(names, avg)))