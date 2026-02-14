import pytest

# Exemplu simplu de fixture
# @pytest.fixture()
# def my_fixture():
#     return ['some', 'test', 'data']

@pytest.fixture()
def my_fixture():
    # Exemplu
    # Aici am putea crea o baza de date pentru testare
    print('\nI am fixture setup')

    # Populam baza de date
    data = ['some', 'test', 'data']
    yield data

    # Stergem baza de date si continutul ei
    print('\nI am fixture tearDown')

def test_first(my_fixture):
    print(f'\nFirst test data: {my_fixture}')

def test_another_test(my_fixture):
    print(f'\nSame data: {my_fixture}')
