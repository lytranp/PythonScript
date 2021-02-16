
string = "hello vietnam"

## TODO: startwith and endwith functions
print(string.upper().startswith("HELLO"))
print(string.endswith("Vietnam")) # case-sensitive

## TODO: find and rfind functions 
print(string.find("he"))
print(string.rfind("he"))
print("he" in string)

##TODO: replace
newStr = string.replace("he", "He")
print(newStr)