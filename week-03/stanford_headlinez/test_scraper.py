import requests
import scraper as cs

SAMPLE_URL = 'https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'
HEADLINE_PATTERN = '<h3><a'

TEST_URL = 'https://compciv.github.io/stash/hello.html'

HED_HTML = """<h3><a href="https://news.stanford.edu/yo/go-card">Small step for man, giant gaffe for NASA</a></h3>"""

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




# kind of dicey to be testing network connections...
# oh well...
def test_fetch_html():
    x = cs.fetch_html(TEST_URL)
    assert isinstance(x, str)
    assert x.strip() == '<h1>Hello, world!</h1>'

def test_extract_headline_text():
    h = cs.extract_headline_text(HED_HTML)

    assert isinstance(h, str)
    assert h == 'Small step for man, giant gaffe for NASA'


def test_parse_headline_tags():
    tags = cs.parse_headline_tags(PAGE_HTML)
    assert isinstance(tags, list)
    assert all(type(t) is str for t in tags)
    assert all(HEADLINE_PATTERN in t for t in tags)


def test_print_hedz(capsys):
    cs.print_hedz(SAMPLE_URL)
    out, err = capsys.readouterr()
    lines = out.splitlines()
    assert lines[0] == 'A window into long-range planning'
    assert lines[1] == '3-D images of artifacts enrich experience for students, faculty'