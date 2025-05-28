#Add two lists element-wise using lambda
List1=[2,3,4,5,6]
List2=[1,2,3,4,5]
result=map(lambda x,y:x+y,List1,List2)
print(list(result))