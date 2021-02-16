## String manipulation 

# TODO: upper and lower

# TODO: split and join functions
string = "hello my name is ly tran"
print(",".join(string.split(" ")))

# TODO: use justification functions to align things
names = ["amy", "john", "michael"]
biggest = max([len(names) for names in names])
for name in names:
    print(name.ljust(biggest+2, "-") + ":")
    print(name.rjust(biggest+2, "-") + ":")
    print(name.center(biggest+2, "-") + ":")

# TODO: Use a translation table to replace characters
sample_str = "hello my name is ly tran"
trans_table = string.maketrans("amnilt", "030187")
print(trans_table)
print(sample_str.translate(trans_table)) # this function takes a key:value




