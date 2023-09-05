from app import add

def test_add():
    assert 2 == add(1,1)

def test_subtract():
    assert 0 == sub(1,1)

def test_multiply():
    assert 10 == multiply(1,10)

def test_divide():
    assert 3 == divide(15,5)
