import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_callBack_force(self):

        def function2(useless, useless2):
            return  # return nothing
        test = parseFile("./tests/simple.csv", {
            "num1": "string",
            "num2": "string",
            "num3": "string"
        }, {
            "lineCallBack": function2
        })
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
