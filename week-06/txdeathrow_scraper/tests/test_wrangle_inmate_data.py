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

from bs4 import BeautifulSoup
from scraper import wrangle_inmate_data_from_tag
from data_helper import DATA_SRC_URL
from urllib.parse import urljoin


def make_tag_fixture():
    """
    This function is used to generate a proper bs4 Tag element
    except with some variations to make sure that the
    given `wrangle_inmate_data_from_tag` can handle
    some of the edge cases, such as extraneous whitespace around text
    and date values where the years are not in 4-digit format
    """

    rawhtml = """<tr>
       <td>999607 </td>
       <td align="center">
            <a href="dr_info/tracybillyjoel.html" title="Offender Information for Billy Tracy">Offender Information</a></td>
       <td>Tracy</td>
       <td>Billy</td>
       <td> 11/30/77</td>
       <td align="center">M</td>
       <td>White</td>
       <td>11/15/2017 </td>
       <td> Bowie</td>
       <td>07/15/2015</td>
     </tr>"""

    soup = BeautifulSoup(rawhtml, 'lxml')
    return soup.select('tr')[0]



INMATE_DICT = wrangle_inmate_data_from_tag(make_tag_fixture())



def test_return_value():
    """
    make sure the return value of wrangle_inate_data_from_tag()
    is a dictionary
    """
    return isinstance(INMATE_DICT, dict)


def test_tdcj_id():
    """
    confirm that it has tdcj_id key
    and that it is expected string value
        and that it is not a number type
        and that it has dealt with extraneous whitespace
    """
    assert 'tdcj_id' in INMATE_DICT.keys()
    assert INMATE_DICT['tdcj_id'] == '999607'


def test_absolute_url():
    """
    confirm that it matches expected absolute URL
    pattern
    """
    url = INMATE_DICT['url']
    href = 'dr_info/tracybillyjoel.html' # this is hard-coded

    assert 'url' in INMATE_DICT.keys()
    assert href in url
    assert url == urljoin(DATA_SRC_URL, href)


def test_first_and_last_names():
    assert 'first_name' in INMATE_DICT.keys()
    assert INMATE_DICT['first_name'] == 'Billy'
    assert 'last_name' in INMATE_DICT.keys()
    assert INMATE_DICT['last_name'] == 'Tracy'


def test_birthdate():
    """
    The fixture in this test case has a somewhat irregular
     birthdate: ' 11/30/77'
    """
    assert 'birthdate' in INMATE_DICT.keys()
    assert INMATE_DICT['birthdate'] == '1977-11-30'


def test_gender():
    assert 'gender' in INMATE_DICT.keys()
    assert INMATE_DICT['gender'] == 'M'


def test_race():
    assert 'race' in INMATE_DICT.keys()
    assert INMATE_DICT['race'] == 'White'

def test_date_received():
    assert 'date_received' in INMATE_DICT.keys()
    assert INMATE_DICT['date_received'] == '2017-11-15'

def test_county():
    assert 'county' in INMATE_DICT.keys()
    assert INMATE_DICT['county'] == 'Bowie'

def test_date_offense():
    assert 'date_offense' in INMATE_DICT.keys()
    assert INMATE_DICT['date_offense'] == '2015-07-15'

def test_age_at_offense():
    assert 'age_at_offense' in INMATE_DICT.keys()
    assert isinstance(INMATE_DICT['age_at_offense'], int)
    assert INMATE_DICT['age_at_offense'] == 38

def test_years_before_death_row():
    assert 'years_before_death_row' in INMATE_DICT.keys()
    assert isinstance(INMATE_DICT['years_before_death_row'], float)
    assert INMATE_DICT['years_before_death_row'] == 2.3
