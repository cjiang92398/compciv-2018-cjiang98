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

from format_helper import txdate_to_iso



def test_that_it_returns_a_string():
    """
    txtdate_to_iso() accepts a string argument and returns
      a string argument
    """
    assert isinstance(txdate_to_iso('12/12/1222'), str)


def test_conversion_to_iso_format():
    """
    Make sure it converts something in MM/DD/YYYY
     to: YYYY-MM-DD
    """
    assert txdate_to_iso('05/11/1977') == '1977-05-11'


def test_handles_truncated_year():
    """
    Handles special case where the date is MM/DD/YY
    and assumes that the year is meant to be in the 20th century
    """
    assert txdate_to_iso('04/10/77') == '1977-04-10'


