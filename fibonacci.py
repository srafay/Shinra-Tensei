# A program that asks the user how many Fibonnaci numbers to generate

def fibonacci(count):
    if (count == 1):
        return [1]
    if (count == 2):
        return [1, 1]
    _fib = [1, 1]
    x = y = _sum = 1
    _count = 2
    while _count < count:
        _sum = x + y
        _fib.append(_sum)
        x = y
        y = _sum
        _count += 1
    return _fib

count = int(input("Count of Fibonacci series: "))
print (fibonacci(count))
