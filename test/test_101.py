# -*- coding: utf-8 -*-

"""
Test case for LC101
"""

import unittest
from utils.construct_tree import BinaryTree
from source_code.LC101_SymmetricTree import Solution


class TestLC101(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC101, self).__init__(*args, **kwargs)
        self.solution = Solution()
        self.root = BinaryTree([1, 2, 2, 3, 4, 4, 3]).root
        self.root1 = BinaryTree([1, 2, 2, 2, "null", 2]).root

    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")

    def setUp(self) -> None:
        print("-- set up --")

    def tearDown(self) -> None:
        print("-- tear down --")

    def test_isSymmetric(self):
        self.assertTrue(self.solution.isSymmetric(self.root))
        self.assertFalse(self.solution.isSymmetric(self.root1))
        self.assertFalse(self.solution.isSymmetric2(self.root1))
        self.assertTrue(self.solution.isSymmetric2(self.root))
        self.assertFalse(self.solution.isSymmetric3(self.root1))
        self.assertTrue(self.solution.isSymmetric3(self.root))
