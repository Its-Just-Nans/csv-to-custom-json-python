import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_parse_from_array(self):
        def function1(value):
            return 'toto{}'.format(','.join(map(str, value)))

        def function2(uselessArg):
            return "arrow"
        test = parseFile([
            "num1,num2,num3,num4",
            "1,2,3,4",
            "4,5,6,7",
            "7,8,9,10"
        ], [
            "num4",
            "text",
            [
                "arrayHereLol",
                [
                    "andHereLol",
                    {
                        "obj": "lol",
                        "num4": "int"
                    }
                ]
            ],
            function1,
            function2,
            {
                "staticValue": "value",
                "num1": "int"
            }
        ])
        self.assertEqual(test, [
            [
                "4",
                "text",
                [
                    "arrayHereLol",
                    [
                        "andHereLol",
                        {
                            "obj": "lol",
                            "num4": 4
                        }
                    ]
                ],
                "toto1,2,3,4",
                "arrow",
                {
                    "staticValue": "value",
                    "num1": 1
                }
            ],
            [
                "7",
                "text",
                [
                    "arrayHereLol",
                    [
                        "andHereLol",
                        {
                            "obj": "lol",
                            "num4": 7
                        }
                    ]
                ],
                "toto4,5,6,7",
                "arrow",
                {
                    "staticValue": "value",
                    "num1": 4
                }
            ],
            [
                "10",
                "text",
                [
                    "arrayHereLol",
                    [
                        "andHereLol",
                        {
                            "obj": "lol",
                            "num4": 10
                        }
                    ]
                ],
                "toto7,8,9,10",
                "arrow",
                {
                    "staticValue": "value",
                    "num1": 7
                }
            ]
        ])
