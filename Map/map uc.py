#Convert all strings to uppercase
def uc(upc):
    return upc
upc=input("Enter the str:")
upc=upc.upper()
uppercase=tuple(map(uc,upc))
for x in uppercase:
    print(x,end="")
