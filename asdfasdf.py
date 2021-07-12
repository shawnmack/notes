
def recursiveCheck(subsearch,subfind,findex):
    print('iteration')
    if findex < 1:
      return True
    lastchr = subfind[findex] 
    if lastchr in subsearch:
      foundIndex = subsearch.index(lastchr)
      print(foundIndex)
      subfind=subfind[0:findex]
      print(subfind)
      subsearch.replace(lastchr,'',1)
      print(findex-1)
      print(subsearch)
      recursiveCheck(subsearch,subfind,findex-1)
    else:
      return False

print(recursiveCheck("ahffaksfajeeubsne","jefaa",4))
