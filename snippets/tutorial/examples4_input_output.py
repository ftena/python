'''
Created on 22/09/2013

@author: link
'''

# 7. Input and Output
# The string module contains a Template class which offers yet another
# way to substitute values into strings.

# One question remains, of course: how do you convert values to
# strings?
# Luckily, Python has ways to convert any value to a string: pass
# it to the repr() or str() functions.

s = 'Hello, world.'
print(str(s))
print(repr(s))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))

for x in range(1, 4):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
    
for x in range(1, 3):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    
print('12'.zfill(5))

print('-3.14'.zfill(7))

print('3.14159265359'.zfill(5))

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

import math

print('The value of PI is approximately {}.'.format(math.pi))

print('The value of PI is approximately {!r}.'.format(math.pi))

# 'f' Fixed point. Displays the number as a fixed-point number. The
# default precision is 6.
print('The value of PI is approximately {0:.3f}.'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    # 'd' Decimal Integer. Outputs the number in base 10.
    print('{0:10} ==> {1:10d}'.format(name, phone))
    # 's' String format. This is the default type for strings and may be omitted.
    # The same: print('{0:10s} ==> {1:10d}'.format(name, phone))
    
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# When a final formal parameter of the form **name is present, it
# receives a dictionary (see Mapping Types - dict)
# http://docs.python.org/3.3/library/stdtypes.html#typesmapping
# str.format(*args, **kwargs)
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# 7.2. Reading and Writing Files

f = open('workfile', 'w')
f = open('workfile', 'r+')

 #==============================================================================
 # When size is omitted or negative, the entire contents of the file 
 # will be read and returned; it's your problem if the file is twice
 # as large as your machine's memory. Otherwise, at most size bytes
 # are read and returned. If the end of the file has been reached,
 # f.read() will return an empty string ('').
 #==============================================================================
print("Read before writting:", f.read())

f.write('This is a test\n')
value = ('the answer', 42)
s = str(value)
print("f.write(s) =",f.write(s))

f.close()

f = open('workfile', 'r+')
print("Read after writting:", f.read(), end='\n(END OF FILE)\n')

# 7.2.2. The pickle Module
import pickle

f.close()
f = open('workfile', 'rb+')

x = [66.25, 333, 333, 1, 1234.5]

pickle.dump(x, f)

class Foo:
    atr = 'This is the attribute in class Foo'

pickle.dump(Foo, f)

f.close()

f = open('workfile', 'rb+')

# The order is important

x = pickle.load(f)
print(x)

myFoo = pickle.load(f)
print(myFoo.atr)