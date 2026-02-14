import pytest
from exemplul_1 import add_numbers, divide_numbers


def test_add_numbers():
    a = 4
    b = 7
    expected = 11

    assert add_numbers(4, 7) == expected


def test_add_numbers_with_negatives():
    assert add_numbers(5, -1) == 4


# def test_add_negative_numbers():
#     assert add_numbers(-5, -1) == -6


def test_divide_numbers_with_zero():
    x = 5
    y = 0

    # "pytest.raises(ZeroDivisionError)"
    # se va astepta ca codul din interiorul lui
    # sa ridice eroarea (exceptia) respectiva
    with pytest.raises(ZeroDivisionError):
        divide_numbers(x, y)
