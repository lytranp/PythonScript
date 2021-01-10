# Prompts the user to enter 2 positive integers and find their gcd
# E.g GCD of 4 and 2 is 2; GCD of 16 and 24 is 8
# 1 is commom divisor but not be GCD. So, whenver a new common divisor is found, it becomes new gcd

n1 = eval(input("Enter first integer: "))
n2 = eval(input("Enter second integer: "))

gcd = 1
k = 2
while k <= n1 and k <= n2:  #if k > one of n, n can not divide by k, so we only need to check when k <= n
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
    k += 1

