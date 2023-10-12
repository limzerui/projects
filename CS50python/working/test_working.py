from working import convert
import pytest

def main():
    test_count()
    test_number()
    test_valueerror


def test_count():
    assert convert("10:30 PM to 8:50 AM")=="22:30 to 08:50"
    assert convert("9:50 AM to 4:45 PM")=="09:50 to 16:45"


def test_number():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("3 PM to 3 AM")=="15:00 to 03:00"

def test_valueerror():
    with pytest.raises(ValueError):
        convert("9 AM - 4 PM")


if __name__=="__main__":
    main()