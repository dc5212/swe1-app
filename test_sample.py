def is_even(n):
    return n%2 == 0

def is_odd(n):
    return n%2 == 1

def test_even():
    assert is_even(12) == True

def test_odd():
    assert is_odd(15) == True
