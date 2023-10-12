from plates import is_valid

def main():
    test_count()
    test_number()
    test_lol()
    test_f()
    test_fd()

def test_count():
    assert is_valid("a")==False
    assert is_valid("Hello")==True
    assert is_valid("hdhdhdhdhdh")==False

def test_number():
    assert is_valid("AA")==True
    assert is_valid("A2")==False
    assert is_valid("2A")==False

def test_lol():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False

def test_f():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False
def test_fd():
    assert is_valid('PI3.14') == False
    assert is_valid('PI3!14') == False
    

if __name__=="__main__":
    main()