import pytest
from calculator import Calculator


# test pentru metoda "add"
def test_add_methode_with_positive_numbers():
    c = Calculator(4, 5)
    assert c.add() == 9


def test_add_methode_with_one_negative_number():
    c = Calculator(-2, 5)
    assert c.add() == 3


def test_add_methode_with_all_numbers_negative():
    c = Calculator(-10, -7)
    assert c.add() == -17


# test pentru metoda "sub", cu "reverse = False"
# def test_sub_method_with_reverse_equal_false():
#     c = Calculator(6, 4)
#     assert c.sub() == 2
#
#
# # test pentru metoda "sub", cu "reverse = True"
# def test_sub_method_with_reverse_equal_true():
#     c = Calculator(6, 4)
#     assert c.sub(True) == -2


@pytest.mark.parametrize(
    "a, b, reverse, expected",
    [
        (6, 4, False, 2),
        (6, 4, True, -2),
    ]
)
def test_sub_parametrized(a, b, reverse, expected):
    c = Calculator(a, b)
    assert c.sub(reverse) == expected


# test pentru metoda "mul"
def test_mul_methode():
    c = Calculator(2, 10)
    assert c.mul() == 20


# test pentru div, reverse = False
def test_div_method_with_reverse_equal_false():
    c = Calculator(50, 2)
    assert c.div() == 25


# test pentru div, reverse = True
def test_div_method_with_reverse_equal_true():
    c = Calculator(2, 50)
    assert c.div(True) == 25


# test pentru div in cazul in care impartim la 0
# -> vrem sa testam ca apare exceptia ZeroDivisionError
def test_div_number_with_zero():
    c = Calculator(9, 0)
    with pytest.raises(ZeroDivisionError):
        c.div()

    c = Calculator(0, 9)
    with pytest.raises(ZeroDivisionError):
        c.div(True)
