import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_simple_test(self):
        test = parseFile("./tests/simple.csv")
        self.assertEqual(test, [
            {
                "num1": "1",
                "num2": "2",
                "num3": "3"
            },
            {
                "num1": "4",
                "num2": "5",
                "num3": "6"
            },
            {
                "num1": "7",
                "num2": "8",
                "num3": "9"
            }
        ])
