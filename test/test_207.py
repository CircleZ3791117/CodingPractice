# -*- coding: utf-8 -*-

import unittest
from source_code.LC207_CourseSchedule import Solution


class TestLC207(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLC207, self).__init__(*args, **kwargs)
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
        print("-- tear down --")

    def test_canFinish(self):
        self.assertEqual(True, self.solution.canFinish(2, [[1, 0]]))
        self.assertEqual(False, self.solution.canFinish(2, [[1, 0], [0, 1]]))
        self.assertEqual(False, self.solution.canFinish(3, [[1, 0], [0, 2], [2, 1]]))
        self.assertEqual(True, self.solution.canFinish(3, [[1, 0], [2, 0]]))
        self.assertEqual(True, self.solution.canFinish2(2, [[1, 0]]))
        self.assertEqual(False, self.solution.canFinish2(2, [[1, 0], [0, 1]]))
        self.assertEqual(False, self.solution.canFinish2(3, [[1, 0], [0, 2], [2, 1]]))
        self.assertEqual(True, self.solution.canFinish2(3, [[1, 0], [2, 0]]))
