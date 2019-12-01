# -*- coding: utf-8 -*-

"""Test case for LC 99."""

import unittest
from source_code.LC99_RecoverBinarySearchTree import Solution
from utils.construct_tree import BinaryTree


class TestLC99(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC99, self).__init__(*args, **kwargs)
        self.solution = Solution()
        self.root1 = BinaryTree([1, 3, "null", "null", 2]).root
        self.root2 = BinaryTree([3, 1, "null", "null", 2]).root
        self.bst = BinaryTree([1])

    @classmethod
    def setUpClass(cls) -> None:
        print("set up class...")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class...")

    def setUp(self) -> None:
        print("-- setup --")

    def tearDown(self) -> None:
        print("-- tear down --")

    def test_recoverTree(self):
        self.solution.recoverTree(self.root1)
        self.assertTrue(self.bst.is_equal_trees(self.root1, self.root2))
