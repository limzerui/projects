from twttr import shorten

def test_default():
    assert shorten("twitter")=="twttr"
    assert shorten("TWITTER")=="TWTTR"

def test_number():
    assert shorten("1234")=="1234"

def test_punctuation():
    assert shorten(",./!")==",./!"