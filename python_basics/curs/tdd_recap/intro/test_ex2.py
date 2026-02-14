import pytest

from ex2 import sum_nums


def test_sum_nums_with_wrong_type():
    nums_test = [1, 'a', 3]

    with pytest.raises(TypeError):
        sum_nums(nums_test, only_even=True)

# Primul parametru este un string
# unde definim variabilele folosite in test(ele vor fi trimise automat in parametrii functiei de test)
# Al doilea parametru un o lista
# un fiecare tuple reprezinta un set de date cu care va fi rulat testul
@pytest.mark.parametrize(
    'nums, only_even, expected',
    [
        ([1, 2, 3, 4], False, 10),
        ([1, 2, 3, 4], True, 6),
        ([6, 3, 10], True, 16)
    ]
)
def test_sum_nums_parametrized(nums, only_even, expected):
    assert sum_nums(nums, only_even) == expected
