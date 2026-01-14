import pytest
from app import divide
def test_divide_valid_branch():
    assert divide(10, 2) == 5
def test_divide_exception_branch():
    with pytest.raises(ValueError):
        divide(10, 0)