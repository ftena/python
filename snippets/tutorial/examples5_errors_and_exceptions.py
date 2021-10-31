'''
Created on 23/09/2013

@author: link
'''

# There are (at least) two distinguishable kinds of errors: syntax
# errors and exceptions.

# Exceptions come in different types, and the type is printed as part
# of the message: the types in the example are ZeroDivisionError,
# NameError and TypeError.

# 10 * (1/0)

# 4 + spam*3

# '2' + 2

# 8.3. Handling Exceptions

execute_input_example = False

if (execute_input_example):
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        
try:
    '2' + 2
# Use this with extreme caution!
except (RuntimeError, TypeError, NameError):
    print("An except clause may name multiple exceptions as a parenthesized tuple")
    pass

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as err:
    print("I/O error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    # The last except clause may omit the exception name(s), to serve
    # as a wildcard. Use this with extreme caution, since it is easy
    # to mask a real programming error in this way! It can also be
    # used to print an error message and then re-raise the exception
    # (allowing a caller to handle the exception as well)
    print("Unexpected error:", sys.exc_info()[0])
    raise

files = ['a', 'b', 'workfile.txt']

for arg in files:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
        
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
    
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
    
# 8.4. Raising Exceptions

execute_raise_example = False
if (execute_raise_example):
    raise NameError('HiThere')

execute_raise_example = False
if (execute_raise_example):
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
    raise
    
# 8.5. User-defined Exceptions

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# In this example, the default __init__() of Exception has been
# overridden. The new behavior simply creates the value attribute.
# This replaces the default behavior of creating the args attribute.

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)

execute_raise_example = False
if (execute_raise_example):
    raise MyError('oops!')

# 8.6. Defining Clean-up Actions

execute_raise_example = False
if (execute_raise_example):
    try:
        raise KeyboardInterrupt
    finally:
        print('Goodbye, world!')
        
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)

divide(2, 0)

execute_raise_example = False
if (execute_raise_example):
    divide("2", "1")

# 8.7. Predefined Clean-up Actions

with open("workfile.txt") as f:
    for line in f:
        print(line, end="")