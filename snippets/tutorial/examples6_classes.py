'''
Created on 23/09/2013

@author: link
'''

import module_example

# 9.2. Python Scopes and Namespaces

# A namespace is a mapping from names to objects.

print("module_example.variable_test:", module_example.variable_test)

module_example.variable_test = 10

print("module_example.variable_test:", module_example.variable_test)

# A scope is a textual region of a Python program where a namespace is directly
# accessible.

# This is an example demonstrating how to reference the different scopes and
# namespaces, and how global and nonlocal affect variable binding:

def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        # If a name is declared global, then all references and
        # assignments go directly to the middle scope containing 
        # the module's global names.
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)    
    do_global()    
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# 9.3. A First Look at Classes

# When a class definition is entered, a new namespace is created, and used as
# the local scope.

# 9.3.2. Class Objects

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'
    
print("MyClass.i:", MyClass.i)
print("---> MyClass.f(MyClass):", MyClass.f(MyClass))
print("---> MyClass.f:", MyClass.f)
print("MyClass.__doc__:", MyClass.__doc__)

# Class instantiation uses function notation.
x = MyClass()

print("x.i:", x.i)
print("---> x.f():", x.f())
print("---> x.f:", x.f)
print("x.__doc__:", x.__doc__)

# When a class defines an __init__() method, class instantiation automatically
# invokes __init__() for the newly-created class instance.

class Complex:
    def __init__(self, realpart, imagpart):
        print('__init__ method in Complex class')
        self.r = realpart
        self.i = imagpart

z = Complex(3.0, -4.5)
print('x.r, x.i:', z.r, z.i)

class MyComplex:
    def __init__(self, realpart, imagpart):        
        self.r = realpart
        self.i = imagpart
    r = 10
    i = 20

z = MyComplex(6.0, -1.5)
print('---> z = MyComplex: x.r, x.i:', z.r, z.i)

print('---> MyComplex.r, MyComplex.i:', MyComplex.r, MyComplex.i)

# 9.3.3. Instance Objects

# Now what can we do with instance objects? The only operations understood by
# instance objects are attribute references. There are two kinds of valid
# attribute names, data attributes and methods.

# **data attributes** correspond to "instance variables" in Smalltalk, and to
# "data members" in C++. Data attributes need not be declared; like local
# variables, they spring into existence when they are first assigned to. For
# example, if x is the instance of MyClass created above, the following piece of
# code will print the value 16, without leaving a trace:
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print('x.counter:', x.counter)
del x.counter

# The other kind of instance attribute reference is a method. A method is a
# function that "belongs to" an object. Valid method names of an instance object
# depend on its class. x.f is not the same thing as MyClass.f - it is a method
# object, not a function object.

# Function object: MyClass.f
# Method object: x.f

print('x.f is a valid method reference', x.f)

# 9.3.4. Method Objects

# x.f()

# x.f is a method object
xf = x.f
print('xf():', xf())

# You may have noticed that x.f() was called without an argument above, even
# though the function definition for f() specified an argument. Actually, you
# may have guessed the answer: the special thing about methods is that the
# object is passed as the first argument of the function. In our example, the
# call x.f() is exactly equivalent to MyClass.f(x). In general, calling a method
# with a list of n arguments is equivalent to calling the corresponding function
# with an argument list that is created by inserting the method's object before
# the first argument.

print('MyClass.f(x):', MyClass.f(x))

# 9.4. Random Remarks

# Data attributes override method attributes with the same name; to avoid
# accidental name conflicts, which may cause hard-to-find bugs in large
# programs, it is wise to use some kind of convention that minimizes the chance
# of conflicts.

# Note that clients may add data attributes of their own to an instance object
# without affecting the validity of the methods, as long as name conflicts are
# avoided.

# There is no shorthand for referencing data attributes (or other methods!) from
# within methods.

# Often, the first argument of a method is called self. This is nothing more
# than a convention: the name self has absolutely no special meaning to Python.

# Any function object that is a class attribute defines a method for instances
# of that class. It is not necessary that the function definition is textually
# enclosed in the class definition: assigning a function object to a local
# variable in the class is also ok. For example:

# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g
    
# Now f, g and h are all attributes of class C that refer to function objects,
# and consequently they are all methods of instances of C - h being exactly
# equivalent to g **Note that this practice usually only serves to confuse the
# reader of a program.**

instance_C = C()

print('instance_C.f():', instance_C.f(100, 200))
print('instance_C.g():', instance_C.g())
print('instance_C.h():', instance_C.h())

print('C.f():', C.f(C, 100, 200))
print('C.g():', C.g(C))
print('C.h():', C.h(C))

# Methods may call other methods by using method attributes of the self
# argument:

class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
        
instance_Bad = Bag()

instance_Bad.add(5)
instance_Bad.addtwice(10)
instance_Bad.add(15)

print('instance_Bad.data:', instance_Bad.data)

# Each value is an object, and therefore has a class (also called its
# type). It is stored as object.__class__.

print('instance_Bad.__class__', instance_Bad.__class__)
print('instance_Bad.data.__class__', instance_Bad.data.__class__)

# 9.5. Inheritance

# class DerivedClassName(BaseClassName):
#    <statement-1>
#    .
#    .
#    .
#    <statement-N>
    
# class DerivedClassName(modname.BaseClassName):

# Execution of a derived class definition proceeds the same as for a
# base class.

# This is used for resolving attribute references: if a requested attribute is
# not found in the class, the search proceeds to look in the base class.

# Derived classes may override methods of their base classes. Because methods
# have no special privileges when calling other methods of the same object, a
# method of a base class that calls another method defined in the same base
# class may end up calling a method of a derived class that overrides it. (For
# C++ programmers: all methods in Python are effectively virtual.)

# An overriding method in a derived class may in fact want to extend rather than
# simply replace the base class method of the same name. There is a simple way to
# call the base class method directly: just call BaseClassName.methodname(self,
# arguments). This is occasionally useful to clients as well. (Note that this only
# works if the base class is accessible as BaseClassName in the global scope.)

# Python has two built-in functions that work with inheritance
#    Use isinstance() to check an instance's type
#    Use issubclass() to check class inheritance

if (issubclass(bool, int)):
    print ('issubclass(bool, int) returns', issubclass(bool, int))
else:
    print (not issubclass(bool, int))

if (not issubclass(float, int)):
    print ('issubclass(float, int) returns', issubclass(float, int))
    
# 9.5.1. Multiple Inheritance
    
# class DerivedClassName(Base1, Base2, Base3):
#    <statement-1>
#    .
#    .
#    .
#    <statement-N>

# 9.6. Private Variables

# "Private" instance variables that cannot be accessed except from inside an
# object don't exist in Python.

# However, there is a convention that is followed by most Python code: a name
# prefixed with an underscore (e.g. _spam) should be treated as a non-public
# part of the API (whether it is a function, a method or a data member). It
# should be considered an implementation detail and subject to change without
# notice.

