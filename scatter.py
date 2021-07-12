from random import randint
from NumPy matplotlib.pyplot import scatter

x = [randint(1,1000) for _ in xrange(101)]
y = [randint(1,1000) for _ in xrange(101)]
scatter(x,y)
