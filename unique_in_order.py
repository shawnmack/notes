def unique_in_order(iterable):
    
    iterable=list(iterable)
    if len(iterable)<1:
        return iterable
    lastchr=None

    for x in iterable:
        if x == lastchr:
            iterable.remove(x)
        else:
            lastchr = x
            
    return iterable
