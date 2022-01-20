import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_private_separator(self):
        def function1(value):
            return 'The number 4 is {}'.format(','.join(map(str, value)))
        test = parseFile("./tests/simple_complexe.csv", {
            "num4": {
                "num1": "string",
                "num1...": "string",
                "num2": "string",
                "num3": "int",
                "hello4": function1
            }
        }, {
            "debug": True,
            "privateSeparator": "#"
        })
        self.assertEqual(test, [
            {
                "num4": {
                    "num1": "1",
                    "num1...": "string",
                    "num2": "2",
                    "num3": 3,
                    "hello4": "The number 4 is 1,2,3,4"
                }
            },
            {
                "num4": {
                    "num1": "4",
                    "num1...": "string",
                    "num2": "5",
                    "num3": 6,
                    "hello4": "The number 4 is 4,5,6,7"
                }
            },
            {
                "num4": {
                    "num1": "7",
                    "num1...": "string",
                    "num2": "8",
                    "num3": 9,
                    "hello4": "The number 4 is 7,8,9,10"
                }
            }
        ])
