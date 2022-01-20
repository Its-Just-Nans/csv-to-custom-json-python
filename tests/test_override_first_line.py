import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_override_first_line(self):
        newFirstLine = ["hello1", "hello2", "hello3", "hello4"]

        def func(value):
            return 'The number 4 is {}'.format(value)
        test = parseFile("./tests/simple_complexe.csv", {
            "num4": {
                "num4": "string",
                "hello1": "string",
                "hello2": "int",
                "hello3": "float",
                "hello4": func
            }
        }, {
            "overrideFirstLine": newFirstLine
        })
        self.assertEqual(test, [
            {
                "num4": {
                    "num4": "string",
                    "hello1": "1",
                    "hello2": 2,
                    "hello3": 3,
                    "hello4": "The number 4 is 4"
                }
            },
            {
                "num4": {
                    "num4": "string",
                    "hello1": "4",
                    "hello2": 5,
                    "hello3": 6,
                    "hello4": "The number 4 is 7"
                }
            },
            {
                "num4": {
                    "num4": "string",
                    "hello1": "7",
                    "hello2": 8,
                    "hello3": 9,
                    "hello4": "The number 4 is 10"
                }
            }
        ])
