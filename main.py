#
#count = 0
#for x in range(0, 1000):
#    if x**2 % 7 == 2:
#        count = count + 1
#        print(x)
#print("count is", count)

import math

def prime_checker(num):
    upper = round(math.sqrt(num))+1
    isprime = True
    for x in range(2, upper):
        #do stuff
        if num % x == 0:
            isprime = False
            print(x)
    print("is prime:", isprime)

prime_checker(101)