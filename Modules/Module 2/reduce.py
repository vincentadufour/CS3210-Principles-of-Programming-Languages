from functools import reduce

print(reduce((lambda x, y: x if x > y else y), [23, 49, 6, 32]))