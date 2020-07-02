#############################
# Idiomatic python code
# ----------------------
# Below is a cheat sheet for writing more idiomatic python code.
#
# Programming idioms? A way to write code.
# Idiomatic python code is referred to as being 'Pythonic.'
# There's typically one preferred way to write idiomatic
# python code. This can be non-obvious for beginners in
# python but they can be picked up and acquired through
# repetitive practice. Learn more about what
# programming idioms are here: http://wiki.c2.com/?ProgrammingIdiom
#
# By Doug Purcell
##############################

# 1: The idiomatic way to looping over a collection and indices
# looping over a collection and indices

cars = ['mercedes', 'bmw', 'honda', 'ford', 'toyota', 'ferrari']

for x in range(len(cars)):
    print(f'{x} --> {cars[x]}')


# Looping over a collection again using enumerate

print()
for index, value in enumerate(cars):
    print(f'{index} --> {value}')


# Unpacking
# ----------
# While we're on this topic we can use the
# following syntax to learn more about what's
# really happening behind the scenes

# swapping variables in python
a = 5
b = 10
temp = a
a = b
b = temp
print(f'a = {a}')
print(f'b = {b}')

"""
In python 3, a new method of extending unpacking was
introduced by PEP 3132: https://www.python.org/dev/peps/pep-3132
Let's take a look at an example because a clean code snippet is
a better explanation than long winded words.
"""
a, *b = 5, [2, 4, 6, 8]
print(f'a = {a}')
print(f'b = {b}')

c, *d = 8, 10, list(range(1, 11))
print(c)
print(d)

# figuring out the order in how unpacking is done

e, f, *g, h = 100, 25,  [15, 100, 200]
print(f'e = {e}')
print(f'f = {f}')
print(f'g = {g}')
print(f'h = {h}')


# Merging dictionaries

fruits = {'a': 'apple', 'c': 'coconut', 'p': 'pineapple'}
veggies = {'b': 'broccoli', 'ca': 'carrot', 't': 'turnip'}


# nasty way to merging one or dictionaries

grub = {}
for f in fruits:
    grub[f] = fruits[f]

for v in veggies:
    grub[v] = veggies[v]
print(grub)

# pythonic way to doing it

fruits = {'a': 'apple', 'c': 'coconut', 'p': 'pineapple'}
veggies = {'b': 'broccoli', 'ca': 'carrot', 't': 'turnip'}

meal = {**fruits, **veggies}
print(meal)


# want to force your function to require keyword arguments?

def require_keyword_args(*, a):
    return 1 * 10


require_keyword_args(a=10)


"""
Need to assign something (for instance Unpacking)
but will not need that variable in use.
Use an underscore '_'
"""

a, _ = 16, 10
print(f'a = {a}')
print(f'_ = {_}')

# create a list of size N of the same type

ones = [1] * 10     # create a list of size 'n' with ones
print(ones)

nested = [[] for _ in range(10)]    # create a nested list
print(nested)

# How to create a string from a list?
# the bad way to do this

str_one = ''
letters = ['h', 'e', 'l', 'l', 'o']
for x in letters:
    str_one += x

print(f'str = {str_one}')

# the better way to do this
joined = ''.join(letters)
print(joined)

# check to see if a variable equals a constant

# bad way to doing it

x, y = 5, 10
if x == 5:
    print(x)
    if y == 10:
        print(y)

# a better way to doing this
if x:
    print(x)
    if y:
        print(y)

# for more resources check this out: https://www.academyx.com/training/classes/python/advanced/


"""
PEP 8 is the de facto code style guide for python. 
--------------------------------------------------
An easy to read version of it is here: https://pep8.org
Conforming your Python code for PEP 8 is a good idea and
helps make your code more consistent when working on projects
with other developers. There's a command line program, 'pycodestyle'
that can check your code for conformance.It can be installed
by doing the following: 

>>> $ pip install pycodestyle

Then, run it on a series of files to get a report of any
violations:

>>> $ pycodestyle file.py

Note, pycodestyle can be used in conjucntion with autopep8 to
automatically reformat code in the PEP 8 style. Install the program
with: 

>>> $ pip install autopep8

Use it to format a file in place with:

>>> $ autopep8 --in-place file.py 

The --in-place flag will cause the program to output the
modified code directly to the console for review. The --aggressive
flag will perform more changes can be applied several times.

"""
