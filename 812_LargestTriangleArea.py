#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2

Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
'''

class Solution(object):
	def largestTriangleArea(self, points):
		"""
		:type points: List[List[int]]
		:rtype: float 
		"""
		return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1] - i[0] * k[1] - j[0] * i[1] - k[0] * j[1])
			for i, j, k in itertools.combinations(points, 3))