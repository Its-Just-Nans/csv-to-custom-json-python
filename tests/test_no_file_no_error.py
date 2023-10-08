import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_debug(self):
        test = parseFile("./tests/not_found.csv", None, {
            "debug": True,
            "error": "no",
        })
        self.assertEqual(test, [])
