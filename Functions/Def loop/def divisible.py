#Divisible by 5 and 3
def divisible():
    for i in range(1,16):
        if(i%3==0 and i%5==0):
            print(i,"is divisible by 3 and 5")
        elif(i%3==0):
            print(i,"is divisible by 3")
        elif(i%5==0):
            print(i,"is divisible by 5")
divisible()