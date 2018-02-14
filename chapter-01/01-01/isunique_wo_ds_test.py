#!/usr/bin/python3

import unittest
import isunique_wo_ds

class Test(unittest.TestCase):
    def setUp(self):
        self.unique_words = ('','0','a','asdwe231', 'e[2cov]\'', 'lamp');
        self.non_unique_words = ('aa','00','121','35435','__');

    def test_unique(self):
        for w in self.unique_words:
            self.assertEqual(isunique_wo_ds.isUnique(w),True)

    def test_non_unique(self):
        for w in self.non_unique_words:
            self.assertEqual(isunique_wo_ds.isUnique(w),False)

if __name__ == "__main__":
    unittest.main()
