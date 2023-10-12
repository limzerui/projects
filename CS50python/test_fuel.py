from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert('3/4')==75
    assert convert('3/10')==30

def test_gauge():
    assert gauge(75)=="75%"
    assert gauge(30)=="30%"
    assert gauge(99)=="F"

def test_ZeroDivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_Value():
    with pytest.raises(ValueError):
        convert("dog")
