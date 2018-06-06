# Ask the user for a number and determine whether the number is prime or not

def isPrime(number):
    if (number % 2 == 0):
        return 0
    else:
        i = 3
        while i < number:
            if (number % i == 0):
                return 0
            else:
                i += 2
        return 1

number = int(input("Enter a number: "))
if isPrime(number):
    print("{} is a prime number!" .format(number))
else:
    print("{} is not a prime number!" .format(number))
