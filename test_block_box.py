from app import add
def test_add_positive_numbers():
    assert add(10, 20) == 30
def test_add_zero_values():
    assert add(0, 0) == 0
def test_add_negative_numbers():
    assert add(-5, 5) == 0