#from collections import *
# Counter - data s
#user_input = input("Enter a string: ")
#coun_char = Counter(user_input)
#print(coun_char)
from collections import namedtuple

#namedtuple
# info = ('Priyanshu, 34, True, 9.8)
#print(info)

info = namedtuple('info', ['name', 'age', 'ismarried', 'number'])
t = info('Priyanshu', 34, True, 9.8)
print(t.name)
print(t.age)
print(t.ismarried)
print(t.number)