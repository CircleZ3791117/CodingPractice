# -*- coding: utf-8 -*-

"""
Test case for LC102.
"""

import unittest
from source_code.LC102_BinaryTreeLevelOrderTraversal import Solution
from utils.construct_tree import BinaryTree


class TestLC102(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC102, self).__init__(*args, **kwargs)
        self.solution = Solution()
        self.root = BinaryTree([3, 9, 20, "null", "null", 15, 7]).root

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

    def test_levelOrder(self):
        self.assertEqual([[3], [9, 20], [15, 7]], self.solution.levelOrder(self.root))
