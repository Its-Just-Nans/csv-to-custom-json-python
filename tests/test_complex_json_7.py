import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_complex_json_7(self):
        def function1(allValues):
            mystring = 'toto{}'.format(','.join(map(str, allValues)))
            return mystring

        def function2(uselessArg):
            return "arrow"

        def function3(allValues):
            mystring = 'hey{}'.format(','.join(map(str, allValues)))
            return mystring
        test = parseFile("./tests/simple_complexe.csv", {
            "hello": [
                {
                    "num4": "int",
                    "num1": "string"
                }
            ],
            "hello2": [
                {
                    "num4": "int",
                    "num3": function3,
                    "num1": [
                        "num4",
                        "text",
                        function1,
                        function2
                    ]
                }
            ]
        })
        self.assertEqual(test, [
            {
                "hello": [
                    {
                        "num4": 4,
                        "num1": "1"
                    }
                ],
                "hello2": [
                    {
                        "num4": 4,
                        "num3": "hey3",
                        "num1": [
                            "4",
                            "text",
                            "toto1,2,3,4",
                            "arrow"
                        ]
                    }
                ]
            },
            {
                "hello": [
                    {
                        "num4": 7,
                        "num1": "4"
                    }
                ],
                "hello2": [
                    {
                        "num4": 7,
                        "num3": "hey6",
                        "num1": [
                            "7",
                            "text",
                            "toto4,5,6,7",
                            "arrow"
                        ]
                    }
                ]
            },
            {
                "hello": [
                    {
                        "num4": 10,
                        "num1": "7"
                    }
                ],
                "hello2": [
                    {
                        "num4": 10,
                        "num3": "hey9",
                        "num1": [
                            "10",
                            "text",
                            "toto7,8,9,10",
                            "arrow"
                        ]
                    }
                ]
            }
        ])
