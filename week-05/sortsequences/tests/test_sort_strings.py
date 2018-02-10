#####
### assuming this file is in a subdirectory
### relative to the modules that are being test, e.g.
###
### mymodule.py
### |__tests/
###       |_____test_this_file.py
###
### The following boilerplate code to get this test file
### to import modules from the  parent directory
### because I am a very naughty programmer
### who doesn't like best practices
###
### credit:
### https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
###
########### BEGIN BOILERPLATE
from inspect import getsourcefile
import os.path
import sys
current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]
sys.path.insert(0, parent_dir)
########### END BOILERPLATE


import sort_strings as foo

def test_reverse_alpha():
	assert foo.reverse_alpha() == ['danny', 'Zero', 'Dax', '199', '12', '100000']


def test_alpha_case_insensitive():
	assert foo.alpha_case_insensitive() == ['100000', '12', '199', 'danny', 'Dax', 'Zero']


def test_by_longest_length():
	assert foo.by_longest_length() == ['12', 'Dax', '199', 'Zero', 'danny', '100000']


def test_filter_and_sort_number_strings():
	assert foo.filter_and_sort_number_strings() == ['100000', '12', '199']


def test_filter_and_sort_number_strings_as_numbers():
    assert foo.filter_and_sort_number_strings_as_numbers() == ['12', '199', '100000']

