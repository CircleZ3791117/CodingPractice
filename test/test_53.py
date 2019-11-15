# Test case for LC 53

from unittest import TestCase
from source_code.LC53_MaximumSubarray import Solution


class TestLC53(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC53, self).__init__(*args, **kwargs)
        self.solution = Solution()

    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class..")

    def setUp(self) -> None:
        print("set up")

    def tearDown(self) -> None:
        print("tear down")

    def test_maxSubArray(self):
        self.assertEqual(6, self.solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
