#STRING METHODS

#CAPITALIZE
txt="hello"
print(txt.capitalize())

txt="WORLD"
print(txt.capitalize())

#CASEFOLD
txt="HELLO"
print(txt.casefold())

txt="world"
print(txt.casefold())

#CENTER
txt="hello"
print(txt.center(10))
print(txt.center(10,"0"))

#COUNT
txt="hello"
print(txt.count("l"))
print(txt.count("l",2,2))

#ENDSWITH
txt="hello world"
print(txt.endswith("hello."))
print(txt.endswith("world"))

#EXPANDTABS
txt="h\te\tl\tlo\t w\tor\tld"
print(txt.expandtabs(5))
print(txt.expandtabs(10))

#FIND
txt="hello world"
print(txt.find("o"))
print(txt.find("d"))

#ASCII
txt="hello"
print(txt.isascii())

txt="1234"
print(txt.isascii())

#UPPER
txt="hello"
print(txt.isupper())

txt="HELLO"
print(txt.isupper())

#ALPHA
txt="hello"
print(txt.isalpha())

txt="1234"
print(txt.isalpha())

#LOWER
txt="hello"
print(txt.islower())

txt="HELLO"
print(txt.islower())

#TITLE
txt="python programming"
print(txt.istitle())

txt="Python Programming"
print(txt.istitle())

#LSTRIP
txt1="Welcome To"
txt=" python programming "
print(txt1,txt.lstrip())

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

#RSTRIP
txt1="Welcome To"
txt=" python programming "
print(txt1,txt.rstrip())

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

#ALNUM
txt="Python123"
print(txt.isalnum())

txt="Python"
print(txt.isalnum())

#JOIN
mytuple=("CPU","GPU","RAM")
print("#".join(mytuple))
print(" and ".join(mytuple))

#STARTSWITH
txt="Python123"
print(txt.startswith("Py"))
print(txt.startswith("123"))

#SPACE
txt=" "
print(txt.isspace())

txt=" 123 "
print(txt.isspace())

#NUMERIC
txt="123"
print(txt.isnumeric())

txt="python"
print(txt.isnumeric())

#DECIMAL
txt="123"
print(txt.isdecimal())

txt="py"
print(txt.isdecimal())

#FORMAT
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt = "For only {price} dollars!"
print(txt.format(price = 2*10))

