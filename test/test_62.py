"""Test case for LC 62"""
# -*- coding: utf-8 -*-

import unittest
from source_code.LC62_UniquePaths import Solution


class TestLC62(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC62, self).__init__(*args, **kwargs)
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

    def test_uniquePaths(self):
        self.assertEqual(3, self.solution.uniquePaths(3, 2))
        self.assertEqual(28, self.solution.uniquePaths(7, 3))