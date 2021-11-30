# Search an element in an ordered list of numbers

def BinarySearch(numbersList, number):
    i = 0
    j = len(numbersList) - 1
    mid = int(j/2)
    
    while i <= j:
        mid = int((j-i)/2 + i)

        # Exceptional case of last element
        if mid == i or mid == j:
            if numbersList[i] == number or numbersList[j] == number:
                return True
            return False
        
        if numbersList[mid] == number:
            return True  
        if numbersList[mid] > number:
            j = mid
        else:
            i = mid
        
    return False

numbersList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

while 1:
    number = int(input("Enter the number requiring search in the list: "))

    if BinarySearch(numbersList, number):
        print ("{} found in the list" .format(number))
    else:
        print ("{} not found in the list" .format(number))


