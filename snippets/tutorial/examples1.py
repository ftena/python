'''
Created on 12/09/2013

@author: link
'''

#===============================================================================
# 3. An Informal Introduction to Python
# 3.1. Using Python as a Calculator
# 3.1.1. Numbers
# 3.1.2. Strings
# 3.1.3. Lists
# 3.2. First Steps Towards Programming
# 4. More Control Flow Tools
# 4.1. if Statements
# 4.2. for Statements
# 4.3. The range() Function
# 4.4. break and continue Statements, and else Clauses on Loops
# 4.5. pass Statements
# 4.6. Defining Functions
# 4.7. More on Defining Functions
# 4.7.1. Default Argument Values
# 4.7.2. Keyword Arguments
# 4.7.3. Arbitrary Argument Lists
# 4.7.4. Unpacking Argument Lists
# 4.7.5. Lambda Forms
# 4.7.6. Documentation Strings
# 4.7.7. Function Annotations
# 4.8. Intermezzo: Coding Style
#===============================================================================

import string

class MyEmptyClass:
    pass

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        #=======================================================================
        # The statement result.append(a) calls a method of the list object
        # result. A method is a function that 'belongs' to an object and is
        # named obj.methodname, where obj is some object (this may be an
        # expression), and methodname is the name of a method that is defined
        # by the object's type. Different types define different methods.
        # Methods of different types may have the same name without causing
        # ambiguity. (It is possible to define your own object types and
        # methods, using classes, see Classes) The method append() shown in
        # the example is defined for list objects; it adds a new element at
        # the end of the list. In this example it is equivalent to
        # result = result + [a], but more efficient.
        #=======================================================================
        result.append(a)
        a, b = b, a+b
    return result

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        # "in" tests whether or not a sequence contains a certain value.
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print(complaint)

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])
        
def cheeseshop2(*arguments, **keywords):    
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

# If there are more lines in the documentation string, the second
# line should be blank, visually separating the summary from the
# rest of the description.
def my_function():
    """Do nothing, but document it.
    
    No, really, it doesn't do anything.
    """
    pass

if __name__ == '__main__':
    print ('Hello World')

    a, b = 0, 1
    while b < 10:
        print(b)
        a, b = b, a+b
        
    a, b = 0, 1
    while b < 1000:
        print(b, end=',')
        a, b = b, a+b
        
    #x = int(input("Please enter an integer: "))
    x = 0

    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

    squares = [1, 2, 4, 9, 16, 25]
    
    print(squares)
    
    fib(2000)
    
    # Coming from other languages, you might object that fib is not a
    # function but a procedure since it doesn't return a value.
    # In fact, even functions without a return statement do return a
    # value, albeit a rather boring one.
    
    print("None: ", fib(0)) 
    
    fib2_2000 = fib2(2000)
    
    print("Fib2 - 2000 = ", fib2_2000)
    
    #ask_ok('Do you really want to quit?')
    
    parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
    
    cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",           
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
    
    cheeseshop2("ANOTHER TEST", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",           
           shopkeeper="Michael Palin",
           client="John Cleese",)
    
    print(my_function.__doc__)
    
    string_t = "This Is A Test"
    
    print(string_t.lower())
    
    # To use the next code we need import "string"
    print(string.ascii_letters)
    