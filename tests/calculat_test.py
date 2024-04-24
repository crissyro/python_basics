import doctest
from unittest import TestCase, main
from simple_calculator import calculat


# добавляет doctest
def load_test(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(calculat))
    return tests
class CalculatTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculat('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculat('5-2'), 3)

    def test_multiply(self):
        self.assertEqual(calculat('5*2'), 10)

    def test_divide(self):
        self.assertEqual(calculat('10/5'), 2)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as context:
            calculat('10007')
        self.assertEqual('Expression must have one signs', context.exception.args[0])

    def test_no_signs(self):
        with self.assertRaises(ValueError) as context:
            calculat('2+2+2')
        self.assertEqual('Expression must have two integer operands and one sign', context.exception.args[0])

    def test_no_integers(self):
        with self.assertRaises(ValueError) as context:
            calculat('0.333 / 0.11')
        self.assertEqual('Expression must have two integer operands and one sign', context.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as context:
            calculat('q+w')
        self.assertEqual('Expression must have two integer operands and one sign', context.exception.args[0])


if __name__ == '__main__':
    main()
