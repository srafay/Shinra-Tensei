# A program that asks the user how many Fibonnaci numbers to generate

def fibonacci(count):
    if (count == 1):
        return [1]
    if (count == 2):
        return [1, 1]
    fib = [1, 1]
    _count = 0
    while _count < count-2:
        fib.append(fib[_count] + fib[_count + 1])
        _count += 1
    return fib

count = int(input("Count of Fibonacci series: "))
print (fibonacci(count))
