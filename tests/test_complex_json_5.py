import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_complex_json_5(self):
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
                    "num1": [
                        {
                            "num3": "string"
                        }
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
                        "num1": [
                            {
                                "num3": "3"
                            }
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
                        "num1": [
                            {
                                "num3": "6"
                            }
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
                        "num1": [
                            {
                                "num3": "9"
                            }
                        ]
                    }
                ]
            }
        ])
