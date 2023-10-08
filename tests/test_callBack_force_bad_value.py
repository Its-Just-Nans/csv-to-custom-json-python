import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_callBack_force_2(self):
        def function1(values):
            return None

        def function2(useless, useless2):
            return None
        test = parseFile("./tests/simple.csv", {
            "num1": "string",
            "num2": function1,
            "num3": "string"
        }, {
            "callBackForce": False,
            "lineCallBack": function2,
            "debug": True,
        })
        self.assertEqual(test, [
            {'num1': '1', 'num2': None, 'num3': '3'},
            {'num1': '4', 'num2': None, 'num3': '6'},
            {'num1': '7', 'num2': None, 'num3': '9'},
        ])
