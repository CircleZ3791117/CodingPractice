#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Testcase for LC64
'''

from source_code.LC64_MinimumSumPath import Solution
import unittest


class TestLC64(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC64, self).__init__(*args, **kwargs)
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

    def test_minPathSum(self):
        self.assertEqual(7, self.solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
