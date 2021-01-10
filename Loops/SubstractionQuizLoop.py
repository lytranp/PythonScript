# Generate 5 questions, after a student answers all of them, report the number of correct answers. 

import random 
import time 

correctCount = 0; # Count the number of correct answers 
count = 0 # Count the number of questions 
NUMBER_OF_QUESTIONS = 5 # Constant 

startTime = time.time()

while count < NUMBER_OF_QUESTIONS:
    randomNumber = random.randint(0, 9)
    guess = eval(input("What is your guess?: "))

    if randomNumber != guess:
        print("Wrong answer. Next question!")
    else:
        print("You got it")
        correctCount += 1

    count += 1

endtime = time.time()
testTime = int(endtime - startTime)

print("Correct count is ", correctCount, "out of ", NUMBER_OF_QUESTIONS, Total time is: ", testTime, " in seconds")