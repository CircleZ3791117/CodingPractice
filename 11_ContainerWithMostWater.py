#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "circlezhou"

"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

class Solution(object):
	def maxArea(self, height):
		"""
		This method is rejected because of TLE(Time Limited Error).
		:type height: List[int]
		:rtype: int
		"""
		i = 0
		container = []
		while i < len(height):
			j = i + 1
			while j < len(height):
				tmp_container = (j - i) * min(height[i], height[j])
				container.append(tmp_container)
				j += 1
			i += 1
		return max(container)

	def maxArea2(self, height):
		"""
		Accepted.
		:type height: List[int]
		:rtype: int
		"""
		max_container = 0
		i = 0
		j = len(height) - 1
		while i < j:
			tmp_container = (j - i) * min(height[i], height[j])
			if tmp_container > max_container:
				max_container = tmp_container
			if height[i] < height[j]:
				i += 1
			else:
				j -= 1
		return max_container


"""
Unit test
"""
import unittest

class TestSolution(unittest.TestCase):
	def test_maxArea(self):
		s = Solution()
		self.assertEqual(s.maxArea([1,8,6,2,5,4,8,3,7]), 49)

	def test_maxArea2(self):
		s = Solution()
		self.assertEqual(s.maxArea2([1,8,6,2,5,4,8,3,7]), 49)

# if __name__ == '__main__':
# 	unittest.main()
