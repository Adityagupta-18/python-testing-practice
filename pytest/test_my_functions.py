import pytest
from my_functions import add, mul, div

def test_add():
    assert add(5,7)==12

def test_mul():
    assert mul(4,7)==28

def test_div():
    assert div(15,3)==5

def test_div_byzero():
    with pytest.raises(ZeroDivisionError):
        div(10,0)

def test_add_strings():
    assert add('aditya','here')=='adityahere'

@pytest.mark.skip(reason='this is a sample test to skip')
def test_skip():
    pass

@pytest.mark.xfail(reason='this is sample test to be get failed')
def test_fail():
    pass
