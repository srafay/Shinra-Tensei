# A random password generator

import string
import random

def getPass(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(length))

length = int(input("Enter the length of password: "))
password = getPass(length)
print (password)
