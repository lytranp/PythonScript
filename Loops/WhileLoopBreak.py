## While True Loop and break statement
# This loop's structure can be simplified if we receive the first input inside the loop
# and break out of the loop if a test shows that the continuation condition is false

theSum = 0
while True: # condition is Boolean value True: ensure body of loop will execute at least once
    data = input("Enter a number or enter to quit: ") 
    if data == "":
        break # cause an exist from the loop
    number = float(data)
    theSum += number 
print(f"The sum is {theSum}")

## Guess game
import random # this is a module and randint is function
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller,larger)
count = 0
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("too small")
    elif userNumber > myNumber:
        print("too large")
    else:
        print(f"You got it in {count} times")
        break