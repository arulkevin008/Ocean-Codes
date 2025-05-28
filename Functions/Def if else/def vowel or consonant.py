#Vowel or consonant
def vowel_or_consonant(char):
    if char.lower() in ["a", "e", "i", "o", "u"]:
        print("Vowel")
    else:
        print("Consonant")
vowel_or_consonant(input("Enter the char: "))
