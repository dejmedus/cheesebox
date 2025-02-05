import unittest
import datetime
from cheesebox.parsers import *

def parsed(expression):
    for parser in all_parsers:
        result = parser.parse(expression)
        if result is not None:
            return result

class TestParserData(unittest.TestCase):

    def test_math(self):
                
        # result should be in decimals
        self.assertEqual(parsed("2 plus 2"), "4")
        self.assertEqual(parsed("two plus two"), "4")
        self.assertEqual(parsed("one and three quarters plus three"), "4.75")
        self.assertEqual(parsed("two plus two minus one half"), "3.5")
        self.assertEqual(parsed("2 + 2"), "4")
        self.assertEqual(parsed("2.5 + 1"), "3.5")
        self.assertEqual(parsed("1/2 + 1"), "1.5")
        self.assertEqual(parsed("1 1/2 + 1"), "2.5")
        self.assertEqual(parsed("1 1/2 plus 1"), "2.5")
        self.assertEqual(parsed("10 minus 5"), "5")
        self.assertEqual(parsed("3 times 3"), "9")
        self.assertEqual(parsed("20 divided by 4"), "5")
        self.assertEqual(parsed("2.4 1 + 4"), "✖ Invalid syntax")

    def test_measurements(self):
        # result should be in fraction
        self.assertEqual(parsed("1 tsp times 2"), "2 tsp")
        self.assertEqual(parsed("one and three quarters tsp plus one"), "2 3/4 tsp")
        self.assertEqual(parsed("2 tsp * 2"), "1 1/3 tbsp")
        self.assertEqual(parsed("1/3 cup + 2"), "2 1/3 c")
        self.assertEqual(parsed("0.33 cup + 2"), "2 1/3 c")
        self.assertEqual(parsed("0.5 cup + 1"), "1 1/2 c")
        self.assertEqual(parsed("2/6 cup + 2"), "2 1/3 c")
        self.assertEqual(parsed("1/4 tsp times 4"), "1 tsp")
        self.assertEqual(parsed("1/2 tsp * 3/4  "), "3/8 tsp")
        self.assertEqual(parsed("48 tsp"), "1 c")
        self.assertEqual(parsed("3 tsp * 4"), "4 tbsp")
        self.assertEqual(parsed("2 tbsp * 8"), "1 c")
        self.assertEqual(parsed("4 qt"), "1 gal")
        self.assertEqual(parsed("2000 g"), "2 kg")
        self.assertEqual(parsed("3000 ml"), "3 l")
        self.assertEqual(parsed("2 2 4 tsp * 2"), "✖ Invalid syntax")

    def test_conversion(self):
        self.assertEqual(parsed("16tsp to cups"), "1/3 c")
        self.assertEqual(parsed("16 tsp to cup"), "1/3 c")
        self.assertEqual(parsed("4 * 4 tsp to cup"), "1/3 c")
        self.assertEqual(parsed("2 * 4 + 8 tsps to cups"), "1/3 c")
        self.assertEqual(parsed("2*4+8tsps to c"), "1/3 c")


    # def test_time(self):
    #     self.assertEqual(time_parser.parse("1:00 + 30 mins"), "1:30")
    #     self.assertEqual(time_parser.parse("1pm + 30 mins"), "1:30pm")
    #     self.assertEqual(time_parser.parse("1pm plus 30min"), "1:30pm")
    #     self.assertEqual(time_parser.parse("4:00 - 1 hour"), "3:00")
    #     self.assertEqual(time_parser.parse("invalid expression"))

    # def test_date(self):
    #     current_month = datetime.datetime.now().strftime("%b")
    #     current_year = datetime.datetime.now().year()

        # self.assertEqual(date_parser.parse("March 20th 2024 + 20"), f"April 9th, 2024")
        # self.assertEqual(date_parser.parse("March 20th plus 2 weeks"), f"April 3rd")
        # if not month, use this month
        # self.assertEqual(date_parser.parse("20th + 20"), f"{current_month} <date>")
        # if not year, use this year
        # self.assertEqual(date_parser.parse("March 20th + 20"), f"April 9th")
        # account for leap years
        # self.assertEqual(date_parser.parse("February 28th 2023 + 1"), "March 1st, 2023")
        # self.assertEqual(date_parser.parse("February 28th 2024 + 1"), "February 29th, 2024")


if __name__ == '__main__':
    unittest.main()