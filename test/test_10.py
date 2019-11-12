import unittest
from source_code.LC10_RegularExpressionMatch import Solution


class TestSolution(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSolution, self).__init__(*args, *kwargs)
        self.test_solution = Solution()

    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass\n")

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass\n")

    def setUp(self):
        print("--setUp--")

    def tearDown(self):
        print("--tearDown--")

    def test_isMatch(self):
        print("Test isMatch() which using recursive method...")
        self.assertEqual(True, self.test_solution.isMatch('aa', 'a*'))
        self.assertEqual(True, self.test_solution.isMatch('ab', '.*'))
        self.assertEqual(True, self.test_solution.isMatch('aab', 'c*a*b*'))
        self.assertEqual(False, self.test_solution.isMatch('mississippi', 'mis*is*p*.'))
        self.assertEqual(True, self.test_solution.isMatch('', ''))

    def test_isMatch2(self):
        print("Test isMatch2() which using top-down dynamic programming method...")
        self.assertEqual(True, self.test_solution.isMatch2('aa', 'a*'))
        self.assertEqual(True, self.test_solution.isMatch2('ab', '.*'))
        self.assertEqual(True, self.test_solution.isMatch2('aab', 'c*a*b*'))
        self.assertEqual(False, self.test_solution.isMatch2('mississippi', 'mis*is*p*.'))
        self.assertEqual(True, self.test_solution.isMatch2('', ''))

    def test_isMatch3(self):
        print("Test isMatch2() which using top-down dynamic programming method...")
        self.assertEqual(True, self.test_solution.isMatch3('aa', 'a*'))
        self.assertEqual(True, self.test_solution.isMatch3('ab', '.*'))
        self.assertEqual(True, self.test_solution.isMatch3('aab', 'c*a*b*'))
        self.assertEqual(False, self.test_solution.isMatch3('mississippi', 'mis*is*p*.'))
        self.assertEqual(True, self.test_solution.isMatch3('', ''))





if __name__ == "__main__":
    unittest.main()
