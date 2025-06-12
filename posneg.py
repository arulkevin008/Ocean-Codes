def pos_neg():
    try:
        n=int(input("Enter the no:"))
        if(n>=0):
            print(n,"is pos")
        else:
            print(n,"is neg")
    except:
        print("Error")
pos_neg()