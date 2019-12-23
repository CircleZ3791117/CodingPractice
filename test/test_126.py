# -*- coding: utf-8 -*-

""" Test case for LC126 """

import unittest
from source_code.LC126_WorldLadderII import Solution


class TestLC126(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC126, self).__init__(*args, **kwargs)
        self.solution = Solution()

    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")

    def setUp(self) -> None:
        print("-- set up --")

    def tearDown(self) -> None:
        print("-- tear down --")

    def test_findLadders(self):
        self.assertEqual([
            ["hit", "hot", "dot", "dog", "cog"],
            ["hit", "hot", "lot", "log", "cog"]
        ], self.solution.findLadders2("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
