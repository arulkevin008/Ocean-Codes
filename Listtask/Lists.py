#####LISTS
##mylist=["MIT","NIT","IIT"]
##print(mylist)
##
#####INDEX
##mylist[0]="Harvard"
##print(mylist)
##
#####INSERT
##mylist.insert(3,"Oxford")
##print(mylist)
##
#####APPEND
##mylist.append("Stanford")
##print(mylist)
##
#####EXTEND
##university=["Princeton","England"]
##mylist.extend(university)
##print(mylist)
##
#####LOOP
##for i in mylist:
##    print(i)
##
#####REMOVE
##mylist.remove("Harvard")
##print(mylist)
##
#####POP
##mylist.pop(4)
##print(mylist)
##
#####DELETE
##del mylist[2]
##print(mylist)
##
#####CLEAR
##mylist.clear()
##print(mylist)


#1.CALCULATE AMOUNTS IN A LIST
##num=[2,4,6,8,0]
##Sum=0
##for i in num:
##    Sum+=i
##print("SUM=",s)

#2.MAXIMUM AMOUNTS IN A LIST
##maximum=[10,50,40,30,20]
##maximum_element=maximum[0]
##for i in maximum:
##    if(i>maximum_element):
##        maximum_element=i
##print(maximum_element,"is the greatest element")
##
###3.MINIMUM AMOUNTS IN A LIST
##minimum=[10,50,40,30,20]
##Sum1=minimum[0]
##for i in minimum:
##    if(i<Sum1):
##        Sum1=i
##print(Sum1,"is the smallest element")
####
###4.ODD AND EVEN NUMBER FROM THE LIST
##a=[1,2,3,4,5,6,7,8,9,0]
##odd=[]
##even=[]
##for i in a:
##    if(i%2==1):
##        odd.append(i)
##    if(i%2==0):
##        even.append(i)
##print("ODD NUMBERS OF THE LIST",odd)    
##print("EVEN NUMBERS OF THE LIST",even)
##
###6.MULTIPLE DATA ITEMS
##data_list=["we","you",2,4,5,12.567,6.99,True,]
##str1_list=[]
##boolean_list=[]
##integer_list=[]
##float_list=[]
##for i in data_list:
##    if type(i) is str:
##        str1_list.append(i)
##    elif type(i) is int:
##        integer_list.append(i)
##    elif type(i) is bool:
##        boolean_list.append(i)
##    elif type(i) is float:
##        float_list.append(i)
##print("String:",str1_list)
##print("Integer:",integer_list)
##print("Boolean:",boolean_list)
##print("Float:",float_list)

Listnum=[2,4,5,6,7]
square_list=[]
for i in Listnum:
    square_list.append(i**i)
    i=0
print(square_list)
