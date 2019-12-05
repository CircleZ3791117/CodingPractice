# -*- coding: utf-8 -*-

"""
Test case for LC107
"""

import unittest
from source_code.LC107_BinaryTreeLevelOrderTraversalII import Solution
from utils.construct_tree import BinaryTree


class TestLC107(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC107, self).__init__(*args, **kwargs)
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

    def test_zigzagLevelOrder(self):
        self.assertEqual([[15, 7], [9, 20], [3]], self.solution.levelOrderBottom(self.root))
