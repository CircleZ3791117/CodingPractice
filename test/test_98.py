# -*- coding: utf-8 -*-

"""
Testcase for LC98
"""

import unittest
from utils.construct_tree import BinaryTree, TreeNode
from source_code.LC98_ValidateBinarySearchTree import Solution


class TestLC98(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC98, self).__init__(*args, **kwargs)
        self.btree1 = BinaryTree([2, 1, 3]).root
        self.btree2 = BinaryTree([5, 1, 4, "null", "null", 3, 6]).root
        self.btree3 = BinaryTree([10, 5, 15, "null", "null", 6, 20]).root
        self.solution = Solution()

    @classmethod
    def setUpClass(cls) -> None:
        print("set up class...")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class...")

    def setUp(self) -> None:
        print("-- set up --")

    def tearDown(self) -> None:
        print("-- tear down --")

    def test_isValidBST(self):
        self.assertTrue(self.solution.isValidBST(self.btree1))
        self.assertFalse(self.solution.isValidBST(self.btree2))
        self.assertFalse(self.solution.isValidBST(self.btree3))
        self.assertFalse(self.solution.isValidBST_recur(self.btree3))
