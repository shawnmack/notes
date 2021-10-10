import copy

def func(x=[]):
    x.append(1)
    return x

func1 = func
func2 = copy.copy(func)
func3 = copy.deepcopy(func)

print(func is func1)
print(func is func2)
print(func is func3)
print(func == func1)
print(func == func2)
print(func == func3)
