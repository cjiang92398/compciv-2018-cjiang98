"""
####  setup_hw.py

****************************************************************************************
WARNING: Running setup_hw.py as described below will overwrite any existing files at the
         file paths specified for this project (e.g. scraper.py, format_helper.py)

In other words, running this script should be a one-time thing, and definitely not
 something you do after having actually done the homework, e.g. finished writing
 scraper.py and format_helper.py, as your versions would get wiped out with the
 starter versions
****************************************************************************************


The setup/bootstrap file for the txdeathrow_scraper assignment,
which can be found here:

https://github.com/compciv/homeworkhome/tree/master/txdeathrow_scraper

Basically, running this Python script, i.e.:

    $  python setup_hw.py

Will download this assignment's starter files from the Github repo,
including the test files, and save it to your "current working directory" --
i.e. the directory from which you run `python setup_hw.py`


When the script finishes running, your current working directory
will be populated with these files (not including setup_hw.py):

    ├── data_helper.py
    ├── format_helper.py
    ├── scraper.py
    └── tests/
        ├── test_calc_years_diff.py
        ├── test_make_absolute_url.py
        ├── test_scraper.py
        ├── test_txdate_to_iso.py
        └── test_wrangle_inmate_data.py

##########################################################
"""

from pathlib import Path
from time import sleep
import requests


GH_DOMAIN = 'https://compciv.github.io'
GH_SUBDIR = 'homeworkhome/txdeathrow_scraper'
GH_BASEURL = GH_DOMAIN + '/' + GH_SUBDIR

SCRIPT_BASENAMES = ['data_helper.py',
    'format_helper.py',
    'scraper.py',
]

TEST_BASENAMES = ['test_calc_years_diff.py',
  'test_make_absolute_url.py',
  'test_scraper.py',
  'test_txdate_to_iso.py',
  'test_wrangle_inmate_data.py',
]


TESTS_SUBDIR_PATH = Path('tests')


def get_url(url):
    """
    Wrapper around requests.get()

    Arguments:
        url: <str>, the URL for something on the web

    Returns:
        <bytes>: Uses the Request.Response.bytes property --
           instead of the .text property, so that the
           downloaded data is returned as <bytes> and not <str>
    """
    resp = requests.get(url)
    if resp.status_code != 200:
        raise RuntimeError("The server at", url, "had a status code of", resp.status_code)
    else:
        return resp.content


def download_and_save(url, dest_path):
    """
    Wrapper around get_url(), provides quick-n-easy
        interface for saving to a given filename.
        Also has lots of print messages to tell
        us what's going on

    Args:
        url: <str> string representing the URL to download from

        filepath: <str> or <pathlib.Path> object to filepath
           to save what's downloaded from URL. Auto-overwrites
           anything at existing filepath. Assumes any
           subdirectories have been made.

    Returns:
        <NoneType>: this function has lots of effects -- e.g.
           saving files to disk -- but doesn't return anything
    """

    dest_path = Path(dest_path)

    print("---------------------")
    print("Downloading from URL:")
    print("\t", url)

    databytes = get_url(url)
    print(" Number of bytes:", len(databytes))

    print("Saving to local path:", dest_path)
    print(" Absolute path:", dest_path.absolute())
    dest_path.write_bytes(databytes)
    print("\n")



def download_starter_scripts():
    """
    Convenience script for downloading the 3 starter
    homework script files/skeletons
    """
    print("Downloading and saving", len(SCRIPT_BASENAMES), 'starter files')
    for fname in SCRIPT_BASENAMES:
        _uparts = [GH_BASEURL, 'starter', fname]
        src_url = '/'.join(_uparts)

        # the starter files are online at the path
        # starter/filename.ext, but they are saved locally
        # as filename.ext
        # e.g. "github.com/etc/starter/data_helper.py"
        # is saved locally as "data_helper.y"
        dest_fname = fname

        # actually download and save
        download_and_save(src_url, dest_fname)



def download_test_scripts():
    """
    Convenience function for downloading
    and saving all the test files
    """

    print("Downloading and saving", len(TEST_BASENAMES), 'test files')

    # make sure this subdirectory already exists:
    print("Creating test subdirectory", TESTS_SUBDIR_PATH, "(unless it exists)")
    TESTS_SUBDIR_PATH.mkdir(exist_ok=True)
    for fname in TEST_BASENAMES:
        _uparts = [GH_BASEURL, 'tests', fname]
        src_url = '/'.join(_uparts)
        dest_fname = TESTS_SUBDIR_PATH.joinpath(fname)

        # actually download and save
        download_and_save(src_url, dest_fname)






if __name__ == '__main__':
    """
    This routine defines what is executed when this script is run from
    the command-line, i.e.

        $ python setup_hw.py

    """
    print("Welcome to the setup_hw.py script!")

    cwd = Path(__file__).parent.absolute()
    print("The absolute path of the current working directory is:")
    print("\t", cwd)

    print("This script downloads a bunch of files from:\n", GH_BASEURL)
    print("And saves them to the current working directory.")
    print("WARNING: It will also overwrite files at existing filepaths:\n")
    for fname in SCRIPT_BASENAMES:
        n = cwd.joinpath(fname)
        print('\t', n)

    print("\n")
    print("You have 3 seconds to hit Ctrl-C to break out of this program")
    print("if you aren't ready to overwrite the above files...\n")

    sleep(2)
    print("About to do work...!")
    sleep(1)

    download_test_scripts()

    print("\n\n\n")
    sleep(1)

    download_starter_scripts()




