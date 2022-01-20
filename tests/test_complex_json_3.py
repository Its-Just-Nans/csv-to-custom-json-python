import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
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
