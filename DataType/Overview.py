## Data types - all types are class
# The string type
# Numeric type
x = .1 + .1 - .2
print('x is {}'.format(x))
from decimal import *
print(Decimal('.10') + Decimal('.10') - Decimal('.20'))
# Bool type
## return False if value = "", None; 0
x = ""
if x:  # if as x is displayed
    print("True") 
else:
    print("False")

## Sequence type
# Python provides some sequence types including lists, tuples, dictionaries
# List is mutable
l = [1,2,3,4,5]
l[0] = 10
for i in l:
    print("i is {}".format(i))
# Tuple is immutable
t = (1,2,3,4,5)
for i in t:
    print("i is {}".format(i))
# Create a sequence using range
x = range(5,20,2)
for i in x:
    print("i is {}".format(i))
# Dictionary is a searchable sequence of key value pairs
x = {"one":1, "two":2, "three":3}
x["three"] = 42
for k, v in x.items():
    print("k: {} and v: {}".format(k, v))

# type() and id()
