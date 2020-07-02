"""
Object oriented programming in Python
-------------------------------------

Python like many modern languages support the OOP paradigm.
Other languages that supports OOP are Java, C++, Ruby, PHP,
and Go to name a few. This paradigm has been used in the
software industry for decades.

Below are some of the benefits of using OOP:
- Leads to modular programs
- Helps companies build software faster
- Makes updating code bases quicker
- It's been tried and tested

Several studies done on OOP:
https://link.springer.com/article/10.1007/BF01200200

What's exactly an OOP language? Many computer scientists
have different opinions on what an OOP language is, but
the general consensus is that an OOP language must have
four of the following:

- information hiding
- data abstraction
- dynamic binding
- inheritance
Source:
http://eislab.gatech.edu/courses/me6754/resources/1999-fulton/chapter9-1.pdf

The main gist of OOP is to program modeling objects
in everyday life. Examples of industry software that
uses OOP is the Django framework for creating websites
in python, and it translates nicely to relational database
management systems.
"""

"""
Let's learn OOP in python through examples
------------------------------------------

a) class definition with the 'class' keyword 
"""


class LightBulb:
    """
    This is a basic class
    example in python. This
    right here is a doctring
    which helps explains what
    the class does.
    """
    def __str__(self):
        return 'Light Bulb'

# let's create an instance of the LightBulb


bulb1 = LightBulb()
print(bulb1)
print(bulb1.__doc__)
print(type(bulb1))

bulb2 = LightBulb()
print(bulb2)


class LightBulb:
    """
    This is the LightBulb class
    with more details. It implements
    a state method to get the current
    state of the LightBulb. It also
    implements the toggle method to switch
    states between the lights. I.e,  the LightBulb
    is currently off but when it's toggled
    the state switches to True.
    """
    def __init__(self):
        self.switch = False

    def state(self):
        return self.switch

    def toggle(self):

        if not self.switch:
            self.switch = True
        else:
            self.switch = False


l1 = LightBulb()
print(l1.state())
l1.toggle()
print(l1.state())
l1.toggle()
print(l1.state())

# how exactly does the self convention work in python?
# The self convention represents an instance of the class
# Sometimes a small snippet of code is worth more than a 1000 words

print('--- The self convention test ---')
print(LightBulb.state(l1))
LightBulb.toggle(l1)
print(LightBulb.state(l1))

# More OOP questions
# ------------------
# Can you have multiple objects?

l2, l3 = LightBulb(), LightBulb()
if l2 == l3:
    print('equal objects')
else:
    print('Not equal objects')

# what's printed in the above if statement?

# to get the address of an object, use the hash() function
print('The hash address of l2 = {}'.format(hash(l2)))
print('The hash address of l3 = {}'.format(hash(l3)))

# Does each object contain the same data

print(l2.state() == l3.state())  # what's printed?

l2 = l3
print(l2 == l3)

print(l2.state())
print(l3.state())
l2.toggle()
print(l2.state())
print(l3.state())  # what's the output here. Why?

l3.toggle()
print(l3.state())
print(l2.state())
