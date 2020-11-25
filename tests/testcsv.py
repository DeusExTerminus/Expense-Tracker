import unittest
from unittest import mock
from csvhandler import csvhandler


class TestCSVHandler(unittest.TestCase):
    # May be worth changing to mock out use of the third part csv module
    # This could remove the need for an actual test file
    def test_csvreader(self):
        D1 = {'type': 'CC'}
        dictCSV = csvhandler.csvreader("/tests", "testfile.csv")
        D2 = next(next(dictCSV))
        self.assertDictEqual(D1, D2)


if __name__ == "__main__":
    unittest.main()
