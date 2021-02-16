## Initialize string
s = "this is a string"
s2 = 'this is also a string'

## Retrieve
s[0]

## Length
len(s)

## There are 2 ways to iterate over a string
# Like the list using range
s = "abc"
for i in range(len(s)):
    print(s[i])
# use For loop
for c in s:
    print(c)

n = 10245.24
print(f"has a price of {n} is ${round(n,1)}")
print("Your salary is $%.2f" %n)
print(f"Your salary is ${n:,.1f}")
