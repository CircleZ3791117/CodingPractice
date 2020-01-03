# -*- coding: utf-8 -*-

import unittest
from source_code.LC199_BinaryTreeRightSideView import Solution
from utils.construct_tree import BinaryTree


class TestLC199(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC199, self).__init__(*args, **kwargs)
        self.solution = Solution()
        self.node = BinaryTree([1, 2, 3, 4, 'null', 'null', 'null', 5]).root

    @classmethod
    def setUpClass(cls) -> None:
        print("Set up class...")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Tear down class...")

    def setUp(self) -> None:
        print("-- set up --")

    def tearDown(self) -> None:
        print("-- tear down --")

    def test_rightSideView(self):
        self.assertEqual([1, 3, 4, 5], self.solution.rightSideView(self.node))
