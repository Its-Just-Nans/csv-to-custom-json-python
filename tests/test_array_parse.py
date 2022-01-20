import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_array_parse(self):
        def function1(allValues):
            mystring = 'toto{}'.format(','.join(map(str, allValues)))
            return mystring

        def function2(uselessArg):
            return "arrow"
        test = parseFile("./tests/simple_complexe.csv", [
            "num4",
            "text",
            function1,
            function2
        ], {
            "arrayParse": False
        })
        self.assertEqual(test, [
            [
                "num4",
                "text",
                "toto1,2,3,4",
                "arrow"
            ],
            [
                "num4",
                "text",
                "toto4,5,6,7",
                "arrow"
            ],
            [
                "num4",
                "text",
                "toto7,8,9,10",
                "arrow"
            ]
        ])
