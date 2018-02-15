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

from format_helper import make_absolute_url

def test_return_type():
    assert isinstance(make_absolute_url('whatev'), str)

def test_absolute_url_match():
    """
    more of a tautology than a test...oh well
    """
    src = 'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_offenders_on_dr.html'
    rel_href = 'something/fun.html'

    abs_url = 'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/' + rel_href
    assert make_absolute_url(rel_href) == abs_url

