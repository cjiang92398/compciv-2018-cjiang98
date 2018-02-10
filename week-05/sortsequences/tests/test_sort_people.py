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

import sort_people as foo

def test_longest_name():
    assert foo.longest_name() == [{'age': 31, 'country': 'France', 'name': 'Gretchen'},
                                 {'age': 17, 'country': 'USA', 'name': 'Barbara'},
                                 {'age': 42, 'country': 'USA', 'name': 'Alice'},
                                 {'age': 55, 'country': 'France', 'name': 'Fran'},
                                 {'age': 24, 'country': 'Canada', 'name': 'Pat'}]


def test_youngest():
    assert foo.youngest() == [{'age': 17, 'country': 'USA', 'name': 'Barbara'},
                             {'age': 24, 'country': 'Canada', 'name': 'Pat'},
                             {'age': 31, 'country': 'France', 'name': 'Gretchen'},
                             {'age': 42, 'country': 'USA', 'name': 'Alice'},
                             {'age': 55, 'country': 'France', 'name': 'Fran'}]

def test_oldest():
	assert foo.oldest() == [{'age': 55, 'country': 'France', 'name': 'Fran'},
                             {'age': 42, 'country': 'USA', 'name': 'Alice'},
                             {'age': 31, 'country': 'France', 'name': 'Gretchen'},
                             {'age': 24, 'country': 'Canada', 'name': 'Pat'},
                             {'age': 17, 'country': 'USA', 'name': 'Barbara'}]



def test_name_reverse_alpha():
	assert foo.name_reverse_alpha() == [{'age': 24, 'country': 'Canada', 'name': 'Pat'},
                                     {'age': 31, 'country': 'France', 'name': 'Gretchen'},
                                     {'age': 55, 'country': 'France', 'name': 'Fran'},
                                     {'age': 17, 'country': 'USA', 'name': 'Barbara'},
                                     {'age': 42, 'country': 'USA', 'name': 'Alice'}]




def test_country_then_age():
	assert foo.country_then_age() == [{'age': 24, 'country': 'Canada', 'name': 'Pat'},
                                     {'age': 31, 'country': 'France', 'name': 'Gretchen'},
                                     {'age': 55, 'country': 'France', 'name': 'Fran'},
                                     {'age': 17, 'country': 'USA', 'name': 'Barbara'},
                                     {'age': 42, 'country': 'USA', 'name': 'Alice'}]


