## There are 2 types of loops:
# definite iteration
# and indefinite iteration until the program determines to stop it

## for loop: control statement that most easily supports definite iteration

for eachPass in range(4):
    print("It's alive!", end = " ")

number = 2
exponential = 3
product = 1
for i in range(exponential):
    product = product * number
    print(product, end = " ")

## Compute sum of a sequence of numbers from a lowers bound through an upper bound
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
thesum = 0
for number in range (lower, upper + 1):
    thesum += number 
print(thesum)

