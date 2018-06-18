# Recursive program to find factorial of a number

def factorial(number):
    if number <= 1:
        return number
    return number * factorial(number-1)
    

number = int(input("Enter a number to get factorial: "))

print ("Factorial of {} is: {}" .format(number, factorial(number)))
