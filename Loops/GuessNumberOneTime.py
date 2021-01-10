import random

number = random.randint(0, 100)

guess = -1
while guess != number:
    guess = eval(input("Enter your guess: "))

    if guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your guess is too small")

print("You got it")