#Leapyear
def leapyear(year):
    try:
        if(year%4==0):
            return year,"is a Leap year"
        else:
            return year,"is not a Leap year"
    except:
        return "Error!"
print(leapyear(2004))
print(leapyear("abcf"))