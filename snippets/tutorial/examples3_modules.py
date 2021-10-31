'''
Created on 22/09/2013

@author: link
'''

# 6. Modules

#===============================================================================
# When a module named spam is imported, the interpreter first searches 
# for a built-in module with that name. If not found, it then searches
# for a file named spam.py in a list of directories given by the variable
# sys.path. sys.path is initialized from these locations:
# 
# - the directory containing the input script (or the current directory).
# - PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
# - the installation-dependent default.
#===============================================================================

# Check PYTHONPATH
import fibo

print(fibo.fib(1000))

print(fibo.fib2(1000))

print(fibo.__name__)

# Other option:
#from root.nested.fibo import fib, fib2
#print(fib(1000))
#print(fib2(1000))

# 6.3. The dir() Function
import sys

print(dir(fibo))

print(dir(sys))

for x in dir(sys.path):
    if x == '__init__':
        print(x)
             
# 6.4. Packages
# Users of the package can import individual modules from the package, for example:
import root.nested.fibo

# This loads a submodule. It must be referenced with its full name.
print(root.nested.fibo.fib(100))
print(root.nested.fibo.fib2(100))

# An alternative way of importing the submodule is:
from root.nested.fibo import fib2
print("Alternative way of importing:", fib2(100))

# Yet another variation is to import the desired function or variable directly:
#from root.nested import fibo
#print("Yet another variation:", fibo.fib2(100))