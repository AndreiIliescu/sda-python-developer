from unittest import TestCase


class SomeTest(TestCase):
    # prima data se apeleaza functia setUp()
    # pentru a creea datele de test
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        print('Ran test setUp')

    # Definim testele
    def test_first(self):
        print(f'my test data: {self.data}')

    # Dupa ce ruleaza testele sa apeleaza metoda tearDown()
    def tearDown(self):
        print('Deleting fixture data...')
