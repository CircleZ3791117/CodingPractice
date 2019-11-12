'''Test LC 42'''

import unittest
from source_code.LC42_WildcardMatching import Solution, Solution2


class TestLC42(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC42, self).__init__(*args, **kwargs)
        self.solution = Solution()
        self.solution2 = Solution2()

    @classmethod
    def setUpClass(cls) -> None:
        print("Set Up class...")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Tear down class...")

    def setUp(self) -> None:
        print("set up...")

    def tearDown(self) -> None:
        print("tear down...")

    def test_isMatch(self):
        self.assertEqual(False, self.solution.isMatch("cb", "?a"))
        self.assertEqual(True, self.solution.isMatch("aa", "*"))
        self.assertEqual(False, self.solution.isMatch("aa", "a"))
        self.assertEqual(True, self.solution.isMatch("adceb", "*a*b"))
        self.assertEqual(False, self.solution.isMatch("acdcb", "a*c?b"))
        self.assertEqual(True, self.solution.isMatch("", "*"))
        self.assertEqual(True, self.solution.isMatch("abefcdgiescdfimde", "ab*cd?i*de"))

    def test_isMatch2(self):
        self.assertEqual(False, self.solution2.isMatch("cb", "?a"))
        self.assertEqual(True, self.solution2.isMatch("aa", "*"))
        self.assertEqual(False, self.solution2.isMatch("aa", "a"))
        self.assertEqual(True, self.solution2.isMatch("adceb", "*a*b"))
        self.assertEqual(False, self.solution2.isMatch("acdcb", "a*c?b"))
        self.assertEqual(True, self.solution2.isMatch("", "*"))
        self.assertEqual(True, self.solution2.isMatch("abefcdgiescdfimde", "ab*cd?i*de"))
        self.assertEqual(True, self.solution2.isMatch("", ""))

