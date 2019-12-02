# -*- coding: utf-8 -*-

"""
Test case for LC100
"""

import unittest
from source_code.LC100_SameTree import Solution3
from utils.construct_tree import BinaryTree

class TestLC100(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC100, self).__init__(*args, **kwargs)
        self.solution = Solution3()
        self.root1 = BinaryTree([1, 2, 3]).root
        self.root2 = BinaryTree([1, 2, 3]).root

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

    def test_isSameTree(self):
        self.assertTrue(self.solution.isSameTree(self.root1, self.root2))