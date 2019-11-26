# -*- coding: utf-8 -*-
'''Test case for LC96'''

import unittest
from source_code.LC96_UniqueBinarySearchTree import Solution

class TestLC96(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC96, self).__init__(*args, **kwargs)
        self.solution = Solution()

    @classmethod
    def setUpClass(cls) -> None:
        print("set up class...")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class...")

    def setUp(self) -> None:
        print("set up...")

    def tearDown(self) -> None:
        print("tear down...")

    def test_numTrees(self):
        self.assertEqual(5, self.solution.numTrees(3))
        self.assertEqual(42, self.solution.numTrees(5))