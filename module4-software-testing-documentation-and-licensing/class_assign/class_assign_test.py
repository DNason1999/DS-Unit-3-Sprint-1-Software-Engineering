import unittest
from datesplitter import DateSplitter

class date_test(unittest.TestCase):
    

    def testsplitter(self):
        ds = DateSplitter()
        date = '02/22/2019'
        self.assertEqual(first=ds.split_dates(date), second=['02', '22', '2019'])

if __name__ == '__main__':
    unittest.main()