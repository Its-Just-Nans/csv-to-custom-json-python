import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_complex_json_8(self):
        def function1(allValues):
            mystring = 'toto{}'.format(','.join(map(str, allValues)))
            return mystring

        def function2(uselessArg):
            return "arrow"
        test = parseFile("./tests/simple_complexe.csv", {
            "num1": [
                "num4",
                "text",
                function1,
                function2
            ]
        })
        self.assertEqual(test, [
            {
                "num1": [
                    "4",
                    "text",
                    "toto1,2,3,4",
                    "arrow"
                ]
            },
            {
                "num1": [
                    "7",
                    "text",
                    "toto4,5,6,7",
                    "arrow"
                ]
            },
            {
                "num1": [
                    "10",
                    "text",
                    "toto7,8,9,10",
                    "arrow"
                ]
            }
        ])
