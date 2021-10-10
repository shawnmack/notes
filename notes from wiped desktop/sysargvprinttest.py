from sys import *

print('brother\n')

var2 = sys.argv

print('from another mother.')

print(var2)


l = [4, 6, 18, 32, 24, 20, 42, 16, 54, 96, 112]

k = [filter(lambda _:_%6==0,l)]
print(k)

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

z = filter(lambda _:_.startswith('b'), names)
print(for x in z: return x)
