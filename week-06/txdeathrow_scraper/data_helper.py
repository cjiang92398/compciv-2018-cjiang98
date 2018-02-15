import os.path
import requests

# a static/archived copy of Texas's "Offenders on Death Row"
DATA_SRC_URL = 'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_offenders_on_dr.html'
# the filename of the saved page
DATA_FILEPATH = 'tx-deathrow-webpage.html'

def fetch_data_from_web():
    """
    This is meant to only run once. It fetches the page and
    saves it to a specified filepath.

    Args:
        None
    Returns:
        The name of the file saved to
    """
    print("Requesting:", DATA_SRC_URL)
    resp = requests.get(DATA_SRC_URL)
    if resp.status_code != 200:
        errmsg = 'Did not get an OK status when requesting: ' + DATA_SRC_URL
        raise RuntimeError(errmsg)
    else:
        print("Requested page successfully.")
        txt = resp.text
        print("Length of text:", len(txt))
        print('Saving to:', DATA_FILEPATH)
        f = open(DATA_FILEPATH, 'w')
        f.write(txt)
        f.close()
        # this function doesn't need to return anything
        # but let's just return the filename for the heck of it
        return DATA_FILEPATH

def get_html():
    """
    Reads the file at DATA_FILEPATH and returns it as a string.
    If DATA_FILEPATH doesn't exist, bootstrap() is run.

    The upshot is that checker.py doesn't have to worry about
       either downloading a file, or opening an existing file on disk.

    Pre-reqs:
        Expects DATA_FILEPATH to exist. If not, throws an error.
    Args:
        None
    Returns:
        str: the contents of the file at DATA_FILEPATH as a big text string
    """
    if not os.path.exists(DATA_FILEPATH):
        fetch_data_from_web()
    f = open(DATA_FILEPATH, 'r')
    txt = f.read()
    f.close()
    return txt


