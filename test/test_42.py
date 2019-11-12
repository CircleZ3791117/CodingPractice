'''Test LC 42'''

import unittest
from source_code.LC42_WildcardMatching import Solution


class TestLC42(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC42, self).__init__(*args, **kwargs)
        self.solution = Solution()

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

