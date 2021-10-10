unbound = 'string'

def funky():
    '''docstringlol'''
    def funkier():
        nonlocal unbound = 'strung out'

print(unbound)
funky()
print(unbound)
