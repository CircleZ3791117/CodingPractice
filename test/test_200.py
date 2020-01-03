# -*- coding: utf-8 -*-

import unittest
from source_code.LC200_NumberOfIslands import Solution


class TestLC200(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC200, self).__init__(*args, **kwargs)
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
        print("-- tear Down --")

    def test_numIslands(self):
        self.assertEqual(1, self.solution.numIslands([['1', '1', '1', '1', '0'],
                                                      ['1', '1', '0', '1', '0'],
                                                      ['1', '1', '0', '0', '0'],
                                                      ['0', '0', '0', '0', '0']]))
