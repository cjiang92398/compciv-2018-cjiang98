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

from format_helper import calc_years_diff


def test_return_type():
    assert isinstance(calc_years_diff('2012-01-01', '2015-05-05'), float)


def test_zero_diff():
    assert calc_years_diff('2012-01-01', '2012-01-01') == 0

def test_decade_diff():
    assert calc_years_diff('2002-05-01', '2012-05-01') == 10

def test_half_year():
    assert calc_years_diff('2017-07-01', '2018-01-01') == 0.5
