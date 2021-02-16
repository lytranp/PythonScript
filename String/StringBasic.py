import string

print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)

string1 = "hello 9vietnam"
string2 = "hellovietnam"
string3 = "1234ly"

result = ",".join([c for c in string1 if c in string.ascii_letters])
print(result) # separate ascii letters in string1 and join them by ","

print(string1.isalnum()) # space is not considered as alpha-numeric
print(string2.isalnum())
print(string3.isalnum()) # combination of alpha and numeric is alpha-numeric

print(string2.isalpha())
print(all([c.isalpha() for c in string1])) #note: function all()

print(string3.isnumeric())
print(all([c.isnumeric() for c in string3]))