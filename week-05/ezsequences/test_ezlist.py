from ezlist import *

def test_foo_hello():
    assert foo_hello() == list

def test_foo_a():
    assert foo_a() == 0

def test_foo_b():
    assert foo_b() == 4

def test_foo_c():
    assert foo_c() == 42

def test_foo_cx():
    assert foo_cx() == list

def test_foo_d():
    assert foo_d() == 'oranges'

def test_foo_e():
    assert foo_e() == 9

def test_foo_f():
    assert foo_f() == 'a;b;c'

def test_foo_g():
    assert foo_g() == [1,2,3,4]

def test_foo_h():
    assert foo_h() == [42, ['apples', 'oranges'], 5]

