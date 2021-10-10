from random import randint
import matplotlib

x = [randint(1,1000) for _ in xrange(101)]
y = [randint(1,1000) for _ in xrange(101)]
scatter(x,y)
