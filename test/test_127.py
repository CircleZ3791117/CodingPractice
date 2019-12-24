# -*- coding: utf-8 -*-

"""Test case for LC127"""

import unittest

from source_code.LC127_WordLadder import Solution

import logging

logging.basicConfig(level=logging.INFO)


class TestLC127(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC127, self).__init__(*args, **kwargs)
        self.solution = Solution()

    @classmethod
    def setUpClass(cls) -> None:
        logging.info("Set up class...")

    @classmethod
    def tearDownClass(cls) -> None:
        logging.info("Tear down class...")

    def setUp(self) -> None:
        logging.info("-- set up --")

    def tearDown(self) -> None:
        logging.info("-- tear down --")

    def test_ladderLength(self):
        self.assertEqual(5, self.solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
        self.assertEqual(0, self.solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
        self.assertEqual(2, self.solution.ladderLength('a', 'c', ['a', 'b', 'c']))
