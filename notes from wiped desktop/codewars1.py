'''def descending_order(num):
    array = list(str(num))
    l1= sorted(array,reverse=True)
    rValue=''
    for x in l1:
        rValue+=x
    return int(rValue)
    
print(descending_order('110865990'))
from statistics import median
def get_middle(s):
    if len(s)%2==0:
        return s[len(s)//2:(len(s)//2)+2]
    else:
        return s[median(range(len(s)))]

print(get_middle('Shawna'))
print(get_middle('Shawn'))
print(get_middle('test'))


def alphabet_position(text):
    for x in text:
        if isalpha(x):
            print(x)

from math import sqrt
def is_square(n):
    if (n > -1) and sqrt(n).is_integer():
        return True
    else:
        return False
print(is_square(25))
''''''
import re

test = 'WUBWUBWUBWUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'

var = test.split('WUB')
'''

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
p
