# -*- coding: utf-8 -*-

import unittest

from source_code.LC130_SurroundedRegions import Solution


class TestLC130(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC130, self).__init__(*args, **kwargs)
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

    def test_solve(self):
        self.assertEqual([['X', 'X', 'X', 'X'],
                          ['X', 'X', 'X', 'X'],
                          ['X', 'X', 'X', 'X'],
                          ['X', 'O', 'X', 'X']], self.solution.solve([['X', 'X', 'X', 'X'],
                                                                      ['X', 'O', 'O', 'X'],
                                                                      ['X', 'X', 'O', 'X'],
                                                                      ['X', 'O', 'X', 'X']]))
