'''
Created on 15/09/2013

@author: link
'''
# 5. Data Structures

a = [66.25, 333, 333, 1, 1234.5]

print(a)

print("length of a =", len(a))

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

print ("display 'a for i in a' =", [a for i in a])

print ("display 'b-5 for b in range(1, 5)' =", [b-5 for b in range(1, 5)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print("[[row[i] for row in matrix] for i in range(4)] =", [[row[i] for row in matrix] for i in range(4)])

del matrix

# The next code returns an error:
# print("[[row[i] for row in matrix] for i in range(4)] =", [[row[i] for row in matrix] for i in range(4)])

# 5.3. Tuples and Sequences

a = 66.25, 333, 333, 1, 1234.5

print("Tuple", a)

# The same below.

a = (66.25, 333, 333, 1, 1234.5)

print("Tuple", a)

print("66.25 in a?", 66.25 in a)

#===============================================================================
# Though tuples may seem similar to lists, they are often used in
# different situations and for different purposes. Tuples are
# immutable, and usually contain an heterogeneous sequence of elements
# that are accessed via unpacking (see later in this section) or
# indexing (or even by attribute in the case of namedtuples).
# Lists are mutable, and their elements are usually homogeneous and are
# accessed by iterating over the list.
#===============================================================================

# 5.4. Sets

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("Basket", basket) # show that duplicates have been removed

print("'apple' in basket?", 'apple' in basket)

a = set('abracadabra')
b = set('alacazabm')

print(a)

print(a - b)

print(a | b)

print(a & b)

print(a ^ b)

# 5.5. Dictionaries

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127

print(tel)

del tel['sape']
tel['irv'] = 4127

print(tel)

print(list(tel.keys()))

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
    
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    # See "format" in 7.1. Fancier Output Formatting 
    print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)
    
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

#===============================================================================
# To change a sequence you are iterating over while inside the loop
# (for example to duplicate certain items), it is recommended that
# you first make a copy. Looping over a sequence does not implicitly
# make a copy. The slice notation makes this especially convenient:
#===============================================================================

words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

print("words", words)

# 5.7. More on Conditions

string1, string2, string3 = '', 'Hammer Dance', 'Trondheim'
non_null = string1 or string2 or string3
print("non null =", non_null)