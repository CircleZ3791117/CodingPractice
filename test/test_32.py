#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Testcase for LC32
"""

import unittest
from source_code.LC32_LongestValidParentheses import Solution, Solution2, Solution3, Solution4


class TestLC32(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC32, self).__init__(*args, **kwargs)
        self.solution = Solution()
        self.solution2 = Solution2()
        self.solution3 = Solution3()
        self.solution4 = Solution4()

    @classmethod
    def setUpClass(cls) -> None:
        print("\n-- set up class --\n")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\n--  tear down class --\n")

    def setUp(self) -> None:
        print("set up")

    def tearDown(self) -> None:
        print("tear down")

    def test_longestValidParenthesis(self):
        print("Test LC32 using brute force method...")
        self.assertEqual(2, self.solution.longestValidParentheses("(()"))
        self.assertEqual(4, self.solution.longestValidParentheses(")()())"))
        self.assertEqual(2, self.solution.longestValidParentheses("()(()"))

    def test_longestValidParenthesis2(self):
        print("Test LC32 using dynamic programming method...")
        self.assertEqual(2, self.solution2.longestValidParentheses("(()"))
        self.assertEqual(4, self.solution2.longestValidParentheses(")()())"))
        self.assertEqual(2, self.solution2.longestValidParentheses("()(()"))

    def test_longestValidParenthesis3(self):
        print("Test LC32 using dynamic programming method...")
        self.assertEqual(2, self.solution3.longestValidParentheses("(()"))
        self.assertEqual(4, self.solution3.longestValidParentheses(")()())"))
        self.assertEqual(2, self.solution3.longestValidParentheses("()(()"))

    def test_longestValidParenthesis4(self):
        print("Test LC32 using LR traverse method...")
        self.assertEqual(2, self.solution4.longestValidParentheses("(()"))
        self.assertEqual(4, self.solution4.longestValidParentheses(")()())"))
        self.assertEqual(2, self.solution4.longestValidParentheses("()(()"))
