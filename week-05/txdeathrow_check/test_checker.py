import bs4
import checker
import data_helper

THE_INMATE_ROWS = checker.get_and_parse_inmate_rows()


def test_data_helper_get_html():
    """
    Makes sure that this returns a str object and that
    it seems to contain the kind of data we expect for this page
    """
    txt = data_helper.get_html()
    assert isinstance(txt, str)
    # sanity checks to make sure the file is what we expect
    # in terms of content
    assert '<h1>Death Row Information</h1>' in txt
    assert 'Information for Eric Williams' in txt

def test_get_and_parse_inmate_rows_returns_list():
    """
    get_and_parse_inmate_rows() should return a list
    """
    assert type(THE_INMATE_ROWS) == list

def test_get_and_parse_inmate_rows_has_tag_objects():
    """
    each item in the list returned by get_and_parse_inmate_rows()
    should be a <bs4.element.Tag> object
    """
    assert all(type(r) == bs4.element.Tag for r in THE_INMATE_ROWS)


def test_get_and_parse_inmate_rows_tag_is_a_table_row():
    """
    Each of the Tag objects in cx.parse_inmate_rows()
    should be derived from <tr> elements in the HTML, i.e.
     have  tag name of 'tr'
    """
    assert all(r.name == 'tr' for r in THE_INMATE_ROWS)


def test_expected_rows_to_be_parsed():
    """
    This is a brittle test that assumes that
    data_helper.DATA_SRC_URL points to the same thing it did
    when this test was created, i.e. we handcounted total
    number of things to find.

    It could fail even if student's code is just fine, if
     for some reason I refreshed the contents of DATA_SRC_URL
     without changing the expected value to be found in the
     assertion below:
    """

    assert len(THE_INMATE_ROWS) == 232


def test_count_inmates_returns_integer():
    """
    count_inmates() is a simple function -- it
      just returns a count of how many inmates are listed
      on the page (the page specified in data_helper)
    """
    assert isinstance(checker.count_inmates(), int)

def test_expected_value_for_count_inmates():
    """
    This should exactly be the same as the previous test, i.e.
    the number of tag items in the list returned by
    get_and_parse_inmate_rows()
    """
    assert len(THE_INMATE_ROWS) == checker.count_inmates()


