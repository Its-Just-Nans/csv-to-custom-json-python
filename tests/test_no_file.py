import unittest

from src.csv_to_custom_json import parseFile


class Test(unittest.TestCase):
    def test_debug(self):
        file = "./tests/not_found.csv"
        try:
            test = parseFile(file, None, {
                "debug": True,
            })
        except Exception as e:
            self.assertEqual(
                e.__str__(), f"Can't access to the file : '{file}'")
