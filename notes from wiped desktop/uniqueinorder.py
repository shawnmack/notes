def unique_in_order(iterable):
    
    iterable=list(iterable)
    if len(iterable)<1:
        return iterable
    lastchr=None
    update=0
    for x in iterable:
        if x == lastchr:
            del iterable[update]
            update+=1
        else:
            lastchr = x
            update+=1
    return iterable

print(unique_in_order(["A","D","D"]))
print(unique_in_order('AAAABBBCCDAABBB'))
