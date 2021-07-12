'''import re
def disemvowel(string_):
    done=False
    while(done):
        print(re.match(r'[AEIOUaeiou]',string_))
        if len(re.search(r'[AEIOUaeiou]',string_))>0:
            x = re.search(r'[AEIOUaeiou]',string_)
            string_.replace(x,'')
        else:
            done=True
    return string_

print(disemvowel('this website gay lmao'))
'''
def disemvowel(string_):
    for x in ['a','e','i','o','u','A','E','I','O','U']:
        string=string_.replace(x,'')
    return string_
print(disemvowel('this website gay lmao'))

    
#string.replace(oldvalue, newvalue, count)
#doesn't modify original string

#re.match returns bools
#re.search looks for
#re.findall
#re.

'''
There is a difference between the use of both functions.
Both return the first match of a substring found in the string, but re.match()
searches only from the beginning of the string and return match object if found.
But if a match of substring is found somewhere in the middle of the string, it returns none. 
While re.search() searches for the whole string even if the string contains multi-lines and
tries to find a match of the substring in all the lines of string.
'''
