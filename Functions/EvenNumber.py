def isEven(number):
    if number % 2 == 0:
        print("{} is an even number".format(number))
    else:
        print("{} is an odd number".format(number))

if __name__ == "__main__":
    number = -1
    while number <= 0:
        number = eval(input("Please enter a positive number: "))
    isEven(number)
    