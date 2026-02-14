import pytest
from ex1 import add_numbers, divide_numbers

def test_add_numbers():
    a = 4
    b = 7
    expected = 11

    assert add_numbers(a, b) == expected

def test_add_numbers_with_negatives():
    assert add_numbers(5, -1) == 4


def test_divide_numbers_with_zero():
    a = 5
    b = 0

    # pytest.raises(ZeroDivisionError)
    # sa va astepta ca codul din interiorul lui
    # sa ridice eroare(exceptia) respectiva
    with pytest.raises(ZeroDivisionError):
        divide_numbers(a, b)
