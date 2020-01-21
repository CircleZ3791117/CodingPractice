# -*- coding: utf-8 -*-

"""
Test case for LC279.
"""

import unittest
from source_code.LC279_PerfectSquares import Solution


class TestLC279(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC279, self).__init__(*args, **kwargs)
        self.solution = Solution()

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

    def test_numSquares(self):
        self.assertEqual(3, self.solution.numSquares(12))
        self.assertEqual(2, self.solution.numSquares(13))
