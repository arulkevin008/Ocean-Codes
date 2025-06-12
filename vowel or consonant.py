#Vowel or Consonant
def vowelorconsonant(char):
    try:
        if char in("a","e","i","o","u"):
            return char,"Vowel"
        else:
            return char,"Consonant"
    except:
        return "Error!"
print(vowelorconsonant("a"))
print(vowelorconsonant("123"))