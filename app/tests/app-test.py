import unittest
from app.src.app import add_two_number


class MyTest(unittest.TestCase):
    def test_add_two_number(self):
        self.assertEqual(add_two_number(1, 1), 2)
        self.assertEqual(add_two_number(1, -1), 0)
        self.assertEqual(add_two_number(0, 0), 0)
        self.assertEqual(add_two_number(-1, -1), -2)
        self.assertEqual(add_two_number(1.0, 1), 4)
        self.assertEqual(add_two_number(1.1, 1.1), 2.2)


if __name__ == '__main__':
    unittest.main()
