# Ask the user for a string and print out whether this string is a palindrome or not

def palindrome(string):
    for i in range(0, len(string)):
        if (string[i] == string[len(string)-i-1]):
            pass
        else:
            return 0
    return 1
            
string = input("Enter a string: ")
if (palindrome(string)):
    print("{} is palindrome!" .format(string))
else:
    print("{} is not a palindrome!" .format(string))
