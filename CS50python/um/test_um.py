from um import count
import pytest

def main():
    test_count()
    test_number()
    test_valueerror


def test_count():
    assert count("um")==1
    assert count("Um")==1


def test_number():
    assert count("yummmy")==0
    assert count("Yummy, um, Thanks")==1

def test_valueerror():
    assert count("um, Um, um")==3


if __name__=="__main__":
    main()