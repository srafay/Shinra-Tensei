# Write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

_list = [element for element in a if element in b]

print ("List after comprehension: {} " .format(_list))

result = []

for number in _list:
    if number not in result:
        result.append(number)

print ("List after duplicates removal: {} " .format(result))
