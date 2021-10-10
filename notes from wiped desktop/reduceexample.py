from functools import *

nums = (1, 3, 7)

print(reduce(lambda x, y: x * 10 + y, nums))

