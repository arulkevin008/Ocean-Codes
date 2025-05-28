#Remove empty string from list using filter
str_list=["Debug","","Console"," "]
def empty_str(x):
    return False if x=="" else True
empty=filter(empty_str,str_list)
for x in empty:
    print(x)