import math
import functools
from random import randint

################################################
# Functional programming and comprehensions
# -----------------------------------------
# Functional programming is a popular paradigm in
# coding. Functional programming aspects of python
# was inspired from Lisp developers who coded in
# python and wanted elements of the language in python.
# One way to learn functional programming in python
# is to juxtapose it with normal procedural code
################################################


"""
Lambdas
--------
These are also known as anonymous functions.
When we create functions in python we use the
'def' keyword followed by the name of the function.
This is not typically the case with anonymous functions.
Instead you'll need to use the lambda keyword.

"""


def equation(x, y):
    return (x * y) / x ** 2


eq1 = equation(5, 10)   # 2.0
eq2 = equation(10, 19)  # 1.9
eq3 = equation(4, 6)    # 1.5

print(eq1)
print(eq2)
print(eq3)

# rewrite the above using lambdas in python

eq4 = lambda x, y: (x * y) / x ** 2
print(eq4)           # prints the lambda's reference in memory
print(eq4(5, 10))    # 2.0
print(eq4(100, 16))  # 0.16
print(eq4(17, 10))   # 0.5882352941176471


def hypo(a, b):
    """
    Computes the hypotenuse of
    a right angled triangle.
    :param a: Leg of the right triangle
    :param b: The other leg of the right triangle
    :return: The result rounded to nearest 2nd number
    """
    return round(math.sqrt(a**2 + b**2), 2)


hypo1 = hypo(5, 10)
hypo2 = hypo(7, 100)
hypo3 = hypo(18, 20)
print(f'hypo1 = {hypo1}')
print(f'hypo2 = {hypo2}')
print(f'hypo3 = {hypo3}')

# let's rewrite the above using a lambda and store it in
# a variable called 'hypot'

hypot = lambda a, b: round(math.sqrt(a**2 + b**2))
print(hypot(5, 17))


def upper_case(the_string):
    """
    Write a function that accepts
    a string and returns it uppercase.
    Make sure to check if argument is
    of type string.
    :param the_string:
    :return:the string uppercase
    """
    if isinstance(the_string, str):
        if the_string.lower():
            return the_string.upper()
        return the_string
    else:
        raise ValueError('Must enter in a string')


upper1 = upper_case('hello World')
upper2 = upper_case('This is a cool example')
upper3 = upper_case('HELLO!')
upper4 = upper_case("I'm leaving in 3, 2, 1 seconds!")
# upper5 = upper_case(10)

print(f'upper1 = {upper1}')
print(f'upper2 = {upper2}')
print(f'upper3 = {upper3}')
print(f'upper4 = {upper4}')
# print(f'upper5 = {upper5}')  This will signal an exception

# rewrite upper_case using a lambda in python
# what are some of the limitations of using a lambda?

the_case = lambda the_string : the_string.upper()
print(the_case('bonjour'))
print(the_case('jaMbo!'))
print(the_case('hello WOrld'))
print(the_case('hoLa'))


"""
Lambdas Lab
-----------

1) Do you need to create a lambda as a statement?
You're free to use Google to conduct your research. Verify
your claims by writing some code snippets. In other words
show me the code. 

2) What is meant that lambdas are 'syntatic' sugar for creating
regular functions? 

3) List 3 pros of using lambda functions? List three cons
of using lambda functions? 

4) Does lambdas have docstrings? 

5) Explain what it means that lambdas are throw away functions
in python. 

"""


# passing a function into another function
# ----------------------------------------
# functions are considered first order objects in python


"""
Lambdas are pretty cool for short one line snippets of code.
However, they're more cooler when you extend their functionality.
This can be done by combining the functionality of lambdas with
other functions such as maps, filter, and reduce.

"""

# Map

"""
map(function, iterable, ...)
----------------------------

- Returns an iterator that applies function to every item
of iterable, yielding the results. 
- If additional iterable arguments are passed then function must
take that many arguments and is applied to the items from all iterables in parallel.
"""


def triple(lis=list(range(1, 11))):
    """
    This function takes
    in a list of numbers
    and multiples those numbers by 3.
    :param lis: the list to pass into the function
    :return: the list with the values tripled
    """
    print(f'The list before: {lis}')
    for index, value in enumerate(lis):
        lis[index] *= 3
    print(f'The list after: {lis}')


triple()

# rewriting the above using a map and lambda
triple_nums = list(map(lambda x: x * 3, list(range(1, 11))))
print(triple_nums)

"""
Lab: 
----
Write a function that has two lists
as the parameters and then returns a new
list that sums the corresponding indices of the
lists together. 

Example:
lis1 = [5, 4, 10]
list2 = [7, 8, 10]
list3 = [12, 12, 20]

Make sure to use one list to do this. Consider
the zip() function:

In [1]: x, y = [5, 10, 100], [100, 20, 15]
In [2]: result1 = zip(x, y)
In [3]: result1
Out[3]: <zip at 0x5870e68>
In [4]: result2 = list(zip(x, y))
In [5]: result2
Out[5]: [(5, 100), (10, 20), (100, 15)]

Once you get the function to work rewrite it using
lambdas and maps
"""


def sum_lists(x=[1, 3, 5], y=[1, 10, 20]):
    """
    Iterates over two lists and sums
    their corresponding values:
    :param x: list one
    :param y: list two
    :return: returns a third list with
    the values of list 1 and 2 summed
    together.
    """
    new_list = []
    if len(x) != len(y):
        raise ValueError('Lists must be same length!')
    for x, y in zip(x, y):
        new_list.append(x + y)
    return new_list


print(sum_lists())


# rewriting the above using a map

sum_of_lists = map(lambda x, y: x + y, [1, 3, 5], [5, 10, 100])

print(list(sum_of_lists))

"""
Filter
------

filter(function, iterable)

- Constructs an iterator from those elements of iterable for
which function returns True.
- Iterable may be either a sequence, a container which supports
iteration, or an iterator.
- If function is None, the identity function is assumed, that
is, all elements of iterable that are false are removed.

"""


def filter_function(x=list(range(1, 11)), y=5):
    """
    :param x: A list
    :param y: The value to compare an element in x to
    :return: A list that contains values greater than y
    """
    new_list = []
    print(x)
    for element in x:
        if element > y:
            new_list.append(element)
    print(new_list)


filter_function()

# Here's the above rewritten using a map
# filter_items = [x for x in range(10)]
filter_example = list(filter(lambda x: x > 5, [x for x in range(10)]))
print(filter_example([5, 10, 100]))

# Reduce
# ------


# def reduce_list(x=[1, 3, 6, 10, 100], y=3.5):
#     """
#     Iterate over a list 'x' and multiply
#     the value by y. From there you can
#     :param x: the list of 'x'
#     :param y: the value to multiply 'y' by
#     :return:
#     """
#     result, num = 1, 0
#     for index, value in enumerate(x):
#         num += (value * y)
#     return num
#
#
# print(reduce_list())
#
# # ???? check up on this
# # More tools in the itertools module
# r1 = functools.reduce((lambda x, y: x * 3.5), [1, 3, 6, 10, 100])
# print(r1)

# If you like the functional programming approach to python
# You can use the itertools module for more solutions
# Learn more about itertools here: https://docs.python.org/3/library/itertools.html

"""
Comprehensions in python
------------------------
They can emulate some of the benefits of using
functional programming in python such as code
succinctness and less typing on the programmer's part.

-- List comprehensions 
-- Generators and yield
-- Set comprehensions
-- Dictionary comprehensions
"""

# List comprehensions
# --------------------
# Let's use the juxtaposition approach
# Example, let's compare the normal way
# to building a list vs a list comprehension

# Example #1
# ----------
# Build a list from 1-10 using a 'for' loop
nums = []
for x in range(1, 11):
    nums.append(x)

# rewrite this using a list comprehension

nums1 = [x for x in range(1, 11)]

# Example # 2
# ------------
# Create a list of 10 random numbers
# The numbers must be within the range of 1-100
# Then, sum all 10 random numbers

random_nums = []
for x in range(10):
    random_nums.append(randint(1, 100))

print(random_nums)
print(sum(random_nums))

# rewriting the above using a list comprehension

random_sum = [randint(1, 100) for x in range(10)]

print(sum(random_sum))

# Example 3
# ----------
# Create a list that includes
# the even numbers from 1-20

evens = []
for x in range(1, 21):
    if x % 2 == 0:
        evens.append(x)


# rewrite the above using a list comprehension

evens_example = [x for x in range(1, 21) if x % 2 == 0]



"""
List comprehension labs
-----------------------

1) Create a list comprehension that generates a nested list

2) Create a list comprehension that prints odd numbers form 1-100

3) Create a list comprehension that prints evens numbers, and nums
divisible by 7

"""

# Generators

# Set comprehensions

empty_set = set()
for x in range(1, 10):
    empty_set.update({x})

print(empty_set)

# Dictionary comprehensions
# -------------------------

mappings = {'a': 1, 'b': 5, 'c': 20}

{key: value ** 2 for key, value in mappings.items()}

print(mappings)