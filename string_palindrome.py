# Ask the user for a string and print out whether this string is a palindrome or not

import timeit

def palindrome(string):
    for i in range(0, len(string)):
        if (string[i] == string[len(string)-i-1]):
            pass
        else:
            return 0
    return 1
            
string = input("Enter a string: ")

start = timeit.timeit()

if (palindrome(string)):
    print("{} is palindrome!" .format(string))
else:
    print("{} is not a palindrome!" .format(string))

end = timeit.timeit()
print ("palindrome() took: {} " .format(end - start))


# Efficient

def fasterPalindrome(string):
    return (string == string[::-1])

start = timeit.timeit()
if (fasterPalindrome(string)):
    print("{} is palindrome!" .format(string))
else:
    print("{} is not a palindrome!" .format(string))
    
end = timeit.timeit()
print ("fasterPalindrome() took: {} " .format(end - start))
