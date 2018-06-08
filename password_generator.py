# A random password generator

import string
import random

def getPass(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(length))

length = int(input("Enter the length of password: "))
password = getPass(length)
print (password)


#import secrets

# A more secure method for generating a cryptographically secure passwords
def getSafePass(length):
    
    #password = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(10))
    
    # Since secrets is not supported in py 3.5, just use SystemRandom()
    password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for x in range(10))
