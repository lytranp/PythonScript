from string import Template 
from datetime import datetime

# TODO: use Template
## 1st way
string_sample = "hello $my name is $ly tran"
template = Template(string_sample) # Template is class; initialize object
output = template.substitute(my = "her", ly = "green") # object with instance method substitute
print(output)
## 2nd way
args = {
    "my": "her",
    "ly": "green"
    }
print(template.substitute(args))

# TODO: use str.format()
name = "ly"
age = 20
print("Output: {}, {}".format(name, age))
print("Output: {var1}, {var2}".format(var1 = name, var2 = age))

# TODO: Use f-strings in python 3.6
product = "apple"
price = 19.99
tax = 0.071
date = datetime(2019,1,1)
print(f"On {date: %B - %d - %Y}")
print(
    f"{product} has a price of {price} with tax {tax:.1%} \
the total is {round(price + (price * tax),2)}"
    )

