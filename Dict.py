MyDict={
    "Monitor":"Zebster",
    "Mouse":"HP",
    "Keyboard":"Dell",
    "Year":2025
}
print(MyDict)
print(type(MyDict))
print(MyDict["Monitor"])
print(MyDict["Keyboard"])
print(type(MyDict["Mouse"]))
print(type(MyDict["Keyboard"]))
print(len(MyDict))
print(MyDict.get("Keyboard"))
print(MyDict.get("Year"))
print(MyDict.keys())
print(MyDict.values())
MyDict["Keyboard"]="Hp"
MyDict["Year"]=2026
MyDict.update({"Company":"HP and Zebster"})
MyDict.update({"Parts":"Keyboard,Monitor,Mouse"})
print(MyDict,"After Update")
print(MyDict.popitem())
print(MyDict.pop("Monitor","After pop"))
for values in MyDict:
    print(values)
MyDict.clear()
print(MyDict,"String is cleared")