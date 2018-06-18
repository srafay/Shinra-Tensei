# Recursive program to find factorial of a number
# p.s. functions are easy, lets use Lambda expressions tonight

from functools import reduce

number = int(input("Enter a number to get factorial: "))

print ("Factorial of {} is: {}" .format(number, reduce(lambda x,y: x*y, range(1, number+1))))
