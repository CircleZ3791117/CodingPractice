# -*- coding: utf-8 -*-

"""
Test case for LC111.
"""

import unittest
from source_code.LC111_MinimumDepthOfBinaryTree import Solution
from utils.construct_tree import BinaryTree


class TestLC111(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC111, self).__init__(*args, **kwargs)
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
        self.assertEqual(2, self.solution.minDepth(self.root))
