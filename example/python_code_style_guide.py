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