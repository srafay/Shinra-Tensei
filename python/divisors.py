# Create a program that asks the user for a number and then
# prints out a list of all the divisors of that number

number = int(input("Enter a number: "))
_list = range(2, number + 1)
divisors = [a for a in _list if number % a == 0]
print("Divisors of {} are: {}" .format(number, divisors))
