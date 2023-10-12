from numb3rs import validate

def main():
    test_count()
    test_number()


def test_count():
    assert validate("127.0.0.1")==True
    assert validate("2222.3.33333.2")==False


def test_number():
    assert validate("cat")==False


if __name__=="__main__":
    main()