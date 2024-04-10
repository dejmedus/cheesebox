import unittest
import datetime
from parsers import *

class TestParserData(unittest.TestCase):

    all_parsers
    def test_math(self):
        self.assertEqual(math_parser.parse("2 plus 2"), 4)
        self.assertEqual(math_parser.parse("10 minus 5"), 5)
        self.assertEqual(math_parser.parse("3 times 3"), 9)
        self.assertEqual(math_parser.parse("20 divided by 4"), 5)
        # self.assertIsNone(math_parser.parse("invalid expression"))

    def test_measurements(self):
        self.assertEqual(measurement_parser.parse("1 tsp times 2"), "2 tsp")
        self.assertEqual(measurement_parser.parse("2 tbsp * 2"), "4 tbsp")
        self.assertEqual(measurement_parser.parse("1/3 cup + 2"), "2 1/3 c")
        self.assertEqual(measurement_parser.parse("2/6 cup + 2"), "2 1/3 c")
        # self.assertEqual(measurement_parser.parse("invalid expression"))

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