import unittest
from parsers import *

class TestParserData(unittest.TestCase):
    def test_math(self):
        self.assertEqual(math_parser.parse("2 plus 2"), 4)
        self.assertEqual(math_parser.parse("10 minus 5"), 5)
        self.assertEqual(math_parser.parse("3 times 3"), 9)
        self.assertEqual(math_parser.parse("20 divided by 4"), 5)
        # self.assertIsNone(math_parser.parse("invalid expression"))

if __name__ == '__main__':
    unittest.main()