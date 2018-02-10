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


import sort_numbers as foo

def test_numerical_order():
	assert foo.numerical_order() == [-1024, -9, 0.77, 3, 42]


def test_reverse_numerical_order():
	return foo.reverse_numerical_order() == [42, 3, 0.77, -9, -1024]


def test_as_absolute_value():
	return foo.as_absolute_value() == [0.77, 3, -9, 42, -1024]


def test_as_inverse_number():
	return foo.as_inverse_number() == [-9, -1024, 42, 3, 0.77]


