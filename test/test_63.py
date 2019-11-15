#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Test case for LC 63'''

import unittest
from source_code.LC63_UniquePathsII import Solution


class TestLC63(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC63, self).__init__(*args, **kwargs)
        self.solution = Solution()

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

    def test_uniquePathsWithObstacles(self):
        self.assertEqual(2, self.solution.uniquePathsWithObstacles([[0, 0, 0],
                                                                    [0, 1, 0],
                                                                    [0, 0, 0]
                                                                    ]))
