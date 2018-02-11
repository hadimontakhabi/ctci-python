#!/usr/bin/python3

import unittest
import isunique

class Test(unittest.TestCase):
    def setUp(self):
        self.unique_words = ('','0','a','asdwe231', 'e[2cov]\'', 'lamp');
        self.non_unique_words = ('aa','00','121','35435','__');

    def test(self):
        for w in self.unique_words:
            self.assertEqual(isunique.isUnique(w),True)
        for w in self.non_unique_words:
            self.assertEqual(isunique.isUnique(w),False)

if __name__ == "__main__":
    unittest.main()
