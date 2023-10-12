from seasons import check


def test_convert():
    assert check("2003-02-25")==("2003", "02", "25")
    assert check("jan 25 2003")==None