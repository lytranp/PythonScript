## Prime number is divide by 1 and itself
## Display 50 prime numbers in 5 lines, each containing 10 numbers

NUMBER_OF_PRIMES = 50 # Number of primes to display
NUMBER_OF_PRIMES_PER_LINE = 10 # Display 10 per line
count = 0 # Count number of prime numbers
number = 2 # a number to test prime number 

while count < NUMBER_OF_PRIMES: 
    ## Check condition to see isPrime = True or False
    ## Once number % a divisor, isPrime = False immediately and break out of loop; then continue increase number (until number < 50) to check
    ## If number % a divisor != 0, continue increase divisor (until divisor <= number/2) to check. Until divisor <= number/2 finishes and not break, isPrime = True; and count increases. Then, then continue increase number (until number < 50) to check
    isPrime = True
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            isPrime = False
            break 
        divisor += 1 
    
    if isPrime: 
        count += 1

        print(format(number, "2d"), end = ' ')
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            print() 

    number += 1

    