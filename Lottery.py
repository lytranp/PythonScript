#Check the player win lottery based on certain rules

import random

# Generate a lottery number
lottery = random.randint(0, 99) #e.g 34
# Get digits from lottery
lotteryDigit1 = lottery // 10  #e.g: 34 /10 = 3; //: integer division
lotteryDigit2 = lottery % 10   # %: remainder

# Prompt user to guess
guess = eval(input("What is your guess (2 digits): "))
# Get digits from user
guessDigit1 = guess // 10
guessDigit2 = guess % 10

# Check the guess
if guess == lottery:
    print("Exact match: you win $10000")
elif (lotteryDigit1 == guessDigit2 and lotteryDigit2 == guessDigit1):
    print("Match all digits regardless of order: you win $3,000")
elif (lotteryDigit1 == guessDigit1 or
       lotteryDigit1 ==  guessDigit2 or
       lotteryDigit2 == guessDigit1 or 
       lotteryDigit2 == guessDigit2):
    print("Match one digit: you win $1,000")
else:
    print("No match.")

