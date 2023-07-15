import unittest
from calculator import add


class CalculatorTest(unittest.TestCase):

    def test_sum(self):
        result=add('5','8')
        self.assertEqual(result, 13)

if __name__ == '__main__':
    unittest.main()
