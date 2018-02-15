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

from scraper import get_inmate_data

### This is more or less an integration test to
### spot-check the expected values given the specified DATA_SRC_URL
### (i.e. this is a very brittle test)
INMATE_DATA = get_inmate_data()

def test_inmate_count():
    assert len(INMATE_DATA) == 232


def test_types():
    """
    make sure the objects are what they should be, i.e.
    return value of get_inmate_data() is a list of dicts
    """
    assert type(INMATE_DATA) == list
    assert all(type(i) == dict for i in INMATE_DATA)


def test_first_listed_inmate_spotcheck():
    i = INMATE_DATA[0]
    assert i['tdcj_id'] == '999608'
    assert i['last_name'] == 'Hudson'
    assert i['birthdate'] == '1982-07-03'
    assert i['url'] == 'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_info/hudsonwilliam.html'


def test_999513_inmate_spotcheck():
    i = next(i for i in INMATE_DATA if i['tdcj_id'] == '999513')
    assert i['county'] == 'Medina'
    assert i['gender'] == 'M'
    assert i['first_name'] == 'Ramiro'
    assert i['date_offense'] == '2001-01-15'
