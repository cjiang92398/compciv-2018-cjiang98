from bs4 import BeautifulSoup
import bs4
import bscraper as bx
import requests

SAMPLE_URL = bx.SAMPLE_URL
TEST_URL = 'https://compciv.github.io/stash/hello.html'

HED_HTML = """<h3>
    <a href="https://news.stanford.edu/yo/go-card">Small step for man, giant gaffe for NASA</a>
</h3>"""

PAGE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <div class="content">
            <div class="post-meta">
              <p class="post-category">University Affairs</p>
              <h3>Not a actual headline</h3>
            </div>
            <h3><a href="https://news.stanford.edu/2018/">Story B</a></h3>
    </div>
    <div class="content">
        <h3><a href="https://news.stanford.edu/2017/">Story A</a></h3>
        <a href="//localhost">bad link</a>
    </div>
</body>
</html>"""

def footag():
    s = BeautifulSoup(HED_HTML, 'lxml')
    return s.select('h3 a')[0]


# kind of dicey to be testing network connections...
# oh well...
def test_fetch_html():
    x = bx.fetch_html(TEST_URL)
    assert isinstance(x, str)
    assert x.strip() == '<h1>Hello, world!</h1>'


def test_extract_headline_data():
    tag = footag()
    d = bx.extract_headline_data(tag)

    assert isinstance(d, dict)
    assert d['title'] == 'Small step for man, giant gaffe for NASA'
    assert d['url'] == 'https://news.stanford.edu/yo/go-card'


def test_parse_headline_tags():
    tags = bx.parse_headline_tags(PAGE_HTML)
    assert isinstance(tags, list)
    assert all(type(t) is bs4.element.Tag for t in tags)
    assert tags[0].text == 'Story B'
    assert tags[1].attrs['href'] == 'https://news.stanford.edu/2017/'

def test_fetch_hedz():
    hx = bx.fetch_hedz(SAMPLE_URL)
    assert isinstance(hx, list)
    assert len(hx) == 2
    assert all(type(h) is dict for h in hx)
    assert hx[0]['url'] == 'https://news.stanford.edu/2018/01/16/window-long-range-planning/'
    assert '3-D images of artifacts enrich experience for students, faculty' in hx[1]['title']
