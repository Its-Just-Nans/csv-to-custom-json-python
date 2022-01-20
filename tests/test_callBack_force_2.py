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
            "callBackForce": True,
            "lineCallBack": function2
        })
        self.assertEqual(test, [
            None,
            None,
            None
        ])
