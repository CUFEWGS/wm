#%% indentation
# aligned  with opening delimiter
foo = long_function_name(var_one, var_two,
                         var_three, vat_four)

def long_function_name(var_one, var_two,
                       var_three, var_four):
    print(var_one)

if (this_is one_thing and
    that_is_another_thing):
    do_something()

my_list = [
    1, 2, 3,
    4, 5, 6,
]

result = some_function_that_takes_argument(
    'a', 'b', 'c',
    'd', 'e', 'f'
)

with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())

income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_load_interest)

#%% Imports
import os
import sys

from subprocess import Popen, PIPE
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

#%% Module Level Duner Names
"""This is the example module

This module does stuff.
"""

from __future__ import barrt_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Bigales'

import os
import sys

# Whitespace in Expressions and Statements
spam(ham[1], {eggs: 2})
foo = (0,)
if x == 4: print(x, y; x, y = y, x)

ham[1:9], ham[1:9:3], ham[9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper + offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

dict['key'] = lst[index]

x = 1
y = 2
long_variable = 3

i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

def munge(input: AnyStr): ...
def munge() -> AnyStr: ...

def complex(real, imag=0.0):
    return magic(r=real, i=imag)

def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

# When to Use Trailing Commas
FILES = ('setup.cfg',)

FILES = [
    'setup.cfg',
    'tox.ini',
    ]

initialize(FILES,
           error = True,
           )

try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)


def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)

if foo.startswith('bar'):
if isinstance(obj, basestring):

#%% PEP 20
def load():
    from menagerie.models import cat as cat_modules
    from menagerie.models import dog as dog_modules
    from menagerie.models import mouse as mouse_modules