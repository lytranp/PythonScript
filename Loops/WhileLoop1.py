## While loop 
# like if but it indicates the sequence of statements might be executed many times as long as the condition remains true

theSum = 0
data = input("Enter a number: ")
while (data!= ""):
    number = float(data)
    theSum += number 
    data = input("Enter a number or enter to quit: ")
print(f"the sum is: {theSum:,.2f}")

## Summation using for loop
theSum = 0 
for number in range(1,10001):
    theSum += number 
print(theSum)

## Summation using while loop
theSum = 0
number = 1  # must explicitly initialize before the loop
while (number < 10001):
    theSum += number 
    number += 1
print(theSum)

## Count down with for loop
for count in range(10):
    print(count, end = " ")

## Count down with while loop
count = 10
while (count > 0):
    print(count, end = " ")
    count -= 1
