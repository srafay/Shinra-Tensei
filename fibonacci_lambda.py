# Generate fibonacci series using lambda functions

from functools import reduce

n=5
reduce(lambda n: lambda x=[1,1], (x, x[0]+x[1]), range(n-1))
