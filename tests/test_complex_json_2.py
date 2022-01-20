import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_complex_json_2(self):
        test = parseFile("./tests/simple_complexe.csv", {
            "num1": {
                "num4": {
                    "num4": "string"
                }
            },
            "num2": "",
            "num3": ""
        })
        self.assertEqual(test, [
            {
                "num1": {
                    "num4": {
                        "num4": "4"
                    }
                },
                "num2": "2",
                "num3": "3"
            },
            {
                "num1": {
                    "num4": {
                        "num4": "7"
                    }
                },
                "num2": "5",
                "num3": "6"
            },
            {
                "num1": {
                    "num4": {
                        "num4": "10"
                    }
                },
                "num2": "8",
                "num3": "9"
            }
        ])
