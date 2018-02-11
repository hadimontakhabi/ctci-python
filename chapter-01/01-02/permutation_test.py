#!/usr/bin/python3

import unittest
import permutation

class TestPermutation(unittest.TestCase):
    def setUp(self):
        pass
    def test(self):
        self.assertEqual(permutation.isPermutation('derjis','idjers'), True)
        self.assertEqual(permutation.isPermutation('dderjis','idjers'), False)
        
if __name__ == "__main__":
    unittest.main()
        
