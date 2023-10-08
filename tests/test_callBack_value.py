import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_callBack_force_2(self):

        def function2(parsedLine, useless2):
            name = list(parsedLine.keys())
            tab = {}
            tab[name[0]] = parsedLine[name[0]] + "1"
            tab[name[1]] = parsedLine[name[1]] + "1"
            tab[name[2]] = parsedLine[name[2]] + "1"
            return tab
        test = parseFile("./tests/simple.csv", {
            "num1": "string",
            "num2": "string",
            "num3": "string"
        }, {
            "callBackForce": True,
            "lineCallBack": function2
        })
        self.assertEqual(test, [
            {
                "num1": "11",
                "num2": "21",
                "num3": "31"
            },
            {
                "num1": "41",
                "num2": "51",
                "num3": "61"
            },
            {
                "num1": "71",
                "num2": "81",
                "num3": "91"
            }
        ])
