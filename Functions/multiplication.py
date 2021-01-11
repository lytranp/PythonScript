def multiplication (number):
    for i in range(1, 5):
        multiplyResult = number * i
        print("{} * {} = {}".format(number, i, multiplyResult))

#if __name__ == "__main__":
#    multiplication(9)

def main():
    multiplication(9)

main()