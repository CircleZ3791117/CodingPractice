import unittest
from source_code.LC10_RegularExpressionMatch import Solution


class TestSolution(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSolution, self).__init__(*args, *kwargs)
        self.test_solution = Solution()

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("--setUp--")

    def tearDown(self):
        print("--tearDown--")

    def test_isMatch(self):
        print("test isMatch()...")
        self.assertEqual(False, self.test_solution.isMatch('aa', 'a'))
        self.assertEqual(True, self.test_solution.isMatch('aa', 'aa'))



if __name__ == "__main__":
    unittest.main()
