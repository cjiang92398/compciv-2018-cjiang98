from ezdict import *

def test_foo_hello():
    assert foo_hello() == dict

def test_foo_a():
    assert foo_a() == 'Melania Trump'

def test_foo_b():
    assert foo_b() == 'Donald'

def test_foo_bx():
    assert foo_bx() == list

def test_foo_c():
    assert foo_c() == 'Trump, Donald'

def test_foo_d():
    assert foo_d() == 9

def test_foo_f():
    assert foo_f() == 'Barron'

def test_foo_g():
    assert foo_g() == 'Melania Trump,Donald,Ivanka,Eric,Tiffany,Barron'

def test_foo_h():
    assert foo_h() == '2017-01-20'

def test_foo_i():
    assert foo_i() == 74

def test_foo_j():
    assert foo_j() == 'http://docquery.fec.gov/cgi-bin/fecimg/?P80001571'