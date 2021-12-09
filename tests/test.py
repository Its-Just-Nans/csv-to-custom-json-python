import unittest

from src.csv_to_custom_json.csv_to_custom_json import parseFile

print("Start tests")

class Test(unittest.TestCase):
    def test_simple_test(self):
        test = parseFile("./tests/simple.csv")
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
    def test_stop_parse_value(self):
        test = parseFile("./tests/simple.csv", {
            "num1": "int",
            "num2": "float",
            "num3": "string"
        }, {
            "parse": False
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
    def test_private_separator(self):
        def function1(value):
            return 'The number 4 is {}'.format(','.join(map(str,value)))
        test = parseFile("./tests/simple_complexe.csv", {
                "num4": {
                    "num1": "string",
                    "num1...": "string",
                    "num2": "string",
                    "num3": "int",
                    "hello4": function1
                }
            },{
            "debug": True,
            "privateSeparator": "#"
        })
        self.assertEqual(test,[
            {
                "num4": {
                    "num1": "1",
                    "num1...": "string",
                    "num2": "2",
                    "num3": 3,
                    "hello4": "The number 4 is 1,2,3,4"
                }
            },
            {
                "num4": {
                    "num1": "4",
                    "num1...": "string",
                    "num2": "5",
                    "num3": 6,
                    "hello4": "The number 4 is 4,5,6,7"
                }
            },
            {
                "num4": {
                    "num1": "7",
                    "num1...": "string",
                    "num2": "8",
                    "num3": 9,
                    "hello4": "The number 4 is 7,8,9,10"
                }
            }
        ])
    def test_private_separator2(self):
        def function1(value):
            return 'The number 4 is {}'.format(','.join(map(str,value)))
        test = parseFile("./tests/simple_complexe.csv", {
                "num4": {
                    "num1": "string",
                    "num1...": "string",
                    "num2": "string",
                    "num3": "int",
                    "hello4": function1
                }
            },{
            "debug": True
        })
        self.assertEqual(test,[
            {
                "num4": {
                    "num1": "1",
                    "num2": "2",
                    "num3": 3,
                    "hello4": "The number 4 is 1,2,3,4"
                }
            },
            {
                "num4": {
                    "num1": "4",
                    "num2": "5",
                    "num3": 6,
                    "hello4": "The number 4 is 4,5,6,7"
                }
            },
            {
                "num4": {
                    "num1": "7",
                    "num2": "8",
                    "num3": 9,
                    "hello4": "The number 4 is 7,8,9,10"
                }
            }
        ])
    def test_parse_value(self):
        test = parseFile("./tests/simple.csv", {
            "num1": "int",
            "num2": "float",
            "num3": "string"
        })
        self.assertEqual(test,[
            {
                "num1": 1,
                "num2": 2,
                "num3": "3"
            },
            {
                "num1": 4,
                "num2": 5,
                "num3": "6"
            },
            {
                "num1": 7,
                "num2": 8,
                "num3": "9"
            }
        ])
    def test_parse_from_array(self):
        def function1(value):
            return 'toto{}'.format(','.join(map(str,value)))
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
    def test_complex_json(self):
        test = parseFile("./tests/simple_complexe.csv", {
            "num1": {
                "num4": ""
            },
            "num2": "",
            "num3": ""
        })
        self.assertEqual(test, [
            {
                "num1": {
                    "num4": "4"
                },
                "num2": "2",
                "num3": "3"
            },
            {
                "num1": {
                    "num4": "7"
                },
                "num2": "5",
                "num3": "6"
            },
            {
                "num1": {
                    "num4": "10"
                },
                "num2": "8",
                "num3": "9"
            }
        ])
    def test_callBack_force(self):
        def function1(values):
            return None
        def function2(useless, useless2):
            return None
        test = parseFile("./tests/simple.csv", {
            "num1": "string",
            "num2": function1,
            "num3": "string"
        }, {
            "lineCallBack": function2,
            "debug": True
        })
        self.assertEqual(test, [
            {
                "num1": "1",
                "num2": None,
                "num3": "3"
            },
            {
                "num1": "4",
                "num2": None,
                "num3": "6"
            },
            {
                "num1": "7",
                "num2": None,
                "num3": "9"
            }
        ])
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
    def test_complex_json_3(self):
        test = parseFile("./tests/simple_complexe.csv", {
            "hello": {
                "uno": {
                    "dos": {
                        "tres": {
                            "num4": "string"
                        }
                    }
                }
            },
            "bonjour": {
                "un": {
                    "deux": {
                        "trois": {
                            "num2": "string",
                            "num1": "int"
                        }
                    }
                }
            },
            "num3": ""
        })
        self.assertEqual(test, [
            {
                "hello": {
                    "uno": {
                        "dos": {
                            "tres": {
                                "num4": "4"
                            }
                        }
                    }
                },
                "bonjour": {
                    "un": {
                        "deux": {
                            "trois": {
                                "num2": "2",
                                "num1": 1
                            }
                        }
                    }
                },
                "num3": "3"
            },
            {
                "hello": {
                    "uno": {
                        "dos": {
                            "tres": {
                                "num4": "7"
                            }
                        }
                    }
                },
                "bonjour": {
                    "un": {
                        "deux": {
                            "trois": {
                                "num2": "5",
                                "num1": 4
                            }
                        }
                    }
                },
                "num3": "6"
            },
            {
                "hello": {
                    "uno": {
                        "dos": {
                            "tres": {
                                "num4": "10"
                            }
                        }
                    }
                },
                "bonjour": {
                    "un": {
                        "deux": {
                            "trois": {
                                "num2": "8",
                                "num1": 7
                            }
                        }
                    }
                },
                "num3": "9"
            }
        ])
    def test_complex_json_4(self):
        test = parseFile("./tests/simple_complexe.csv", {
            "hello": [
                {
                    "num4": "int",
                    "num1": "string"
                }
            ],
            "num3": ""
        }, {
            "debug" : "test_complex_json_4"
        })
        self.assertEqual(test, [
            {
                "hello": [
                    {
                        "num4": 4,
                        "num1": "1"
                    }
                ],
                "num3": "3"
            },
            {
                "hello": [
                    {
                        "num4": 7,
                        "num1": "4"
                    }
                ],
                "num3": "6"
            },
            {
                "hello": [
                    {
                        "num4": 10,
                        "num1": "7"
                    }
                ],
                "num3": "9"
            }
        ])
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
    def test_complex_json_6(self):
        test = parseFile("./tests/simple_complexe.csv", {
            "hello": [
                {
                    "num4": "int",
                    "num1": "string"
                }
            ],
            "hello2": [
                [
                    {
                        "num3": "string"
                    }
                ]
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
                    [
                        {
                            "num3": "3"
                        }
                    ]
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
                    [
                        {
                            "num3": "6"
                        }
                    ]
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
                    [
                        {
                            "num3": "9"
                        }
                    ]
                ]
            }
        ])

if __name__ == '__main__':
    unittest.main()
