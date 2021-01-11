def greeting():
    print("----------------")
    print("Hello World")
    print("----------------")

def sum_two_numbers(number1, number2):
    total = number1 + number2 
    print("{} + {} = {}".format(number1, number2, total))

def num_square(num):
    return num * num 

if __name__ == "__main__":
    greeting()
    sum_two_numbers(3, 5)
    print(num_square(3))