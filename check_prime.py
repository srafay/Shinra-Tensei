# Ask the user for a number and determine whether the number is prime or not

import timeit
import math

def isPrime(number):
    if (number % 2 == 0):
        return False
    else:
        i = 3
        while i < number:
            if (number % i == 0):
                return False
            else:
                i += 2
        return True

number = int(input("Enter a number: "))

start = timeit.timeit()

result = isPrime(number)

end = timeit.timeit()
print ("isPrime() took: {} " .format(start - end))

if result:
    print("{} is a prime number!" .format(number))
else:
    print("{} is not a prime number!" .format(number))


def sqrtPrime(number):
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False
    i = 5
    sqrt = math.sqrt(number)
    while i < sqrt:
        if number % i == 0:
            return False
        i += 2
    return True

_start = timeit.timeit()

result = isPrime(number)

_end = timeit.timeit()
print ("sqrtPrime() took: {} " .format(_start - _end))


print ("Speed up is {} " .format((start - end) / (_start - _end)))
