#Use while Loop until user's answer is correct
import random 

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number2 > number1:
    number1, number2 = number2, number1 

answer = eval(input("What is " + str(number2) + " - " + str(number1) + "?"))

while number2 - number1 != answer:
    answer = eval(input("Your answer is wrong!. What is " + str(number2) + " - " + str(number1) + "?"))

print("You got it!")

