#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from source_code.LC94_BinaryTreeInorderTraversal import Solution
from utils.construct_tree import BinaryTree, TreeNode


class TestLC94(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC94, self).__init__(*args, **kwargs)
        self.solution = Solution()
        self.binary_tree = BinaryTree([1, "null", 2, 3]).root

    @classmethod
    def setUPClass(cls) -> None:
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")

    def setUp(self) -> None:
        print("-- set up --")

    def tearDown(self) -> None:
        print("-- tear down --")

    def test_inorderTraversal(self):
        self.assertEqual([1, 3, 2], self.solution.inorderTraversal(self.binary_tree))

    def test_inorder_traverse_nonrecursive(self):
        self.assertEqual([1, 3, 2], self.solution.inorder_traverse_nonrecursive(self.binary_tree))