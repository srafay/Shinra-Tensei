# Write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

_list = [number for number in a if number in b]
print("Might contain duplicates: {}" .format(_list) )

# Without duplicates, user sets
# A set contains an unordered collection of unique and immutable objects
    
print("Without duplicates: {}" .format(set(a) & set(b)) )
