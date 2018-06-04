# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user
# Extra
    # If the number is a multiple of 4, print out a different message
    # Ask the user for two numbers: one number to check (call it num) and one number to divide by (check)
    # If check divides evenly into num, tell that to the user. If not, print a different appropriate message

number = int(input("Enter a number: "))
if( number % 2 != 0 ):
    print("Number is Odd")
elif(number % 4 == 0):
    print("Number is divisible by 4")
else:
    print("Number is Even")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if (num1 % num2 == 0):
    print ("{} is evenly divisible by {}".format(num1, num2))
else:
    print ("{} is not evenly divisible by {}".format(num1, num2))
