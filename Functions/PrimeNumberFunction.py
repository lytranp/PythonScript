def printPrimeNumbers(numberOfPrimes):
    count = 0
    number = 2
    NUMBER_OF_PRIMES_PER_LINE = 10

    while count < numberOfPrimes:
        if isPrimeNumber(number):
            count += 1
            print(number, end = ' ')
            if count % NUMBER_OF_PRIMES_PER_LINE == 0:
               print()

        number += 1 # Check if the next number is prime

def isPrimeNumber(n):
    divisor = 2
    while divisor <= n / 2:
        if n % divisor == 0:
            return False
        divisor += 1

    return True 
    
def main():
    print("The first 50 prime numbers are")
    printPrimeNumbers(50)

main() 