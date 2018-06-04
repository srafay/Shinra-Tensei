# Create a program that asks the user to enter their name and their age
# Print out a message addressed to them that tells them the year that they will turn 100 years old
import datetime

name = input("Enter your name: ")
age = input("Enter your age: ")

now = datetime.datetime.now()
#now.year, now.month, now.day, now.hour, now.minute, now.second

print("\nYou will be 100 years old in the year: " + str((100 - int(age) + now.year)))