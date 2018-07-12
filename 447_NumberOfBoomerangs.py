#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''


# Wrong answer - Reason: not understand the question(requirement)
class Solution(object):
	def numberOfBoomerangs(self, points):
		"""
		:type points: List[List[int]]:
		:rtype: int
		"""
		total_points = len(points)
		if total_points < 3:
			return 0
		boom_points = 0
		for i in range(len(points)):
			tmp = points[i]
			if i == 0:
				p_list = points[1:]
				if self.whetherDistanceAllEqual(tmp, p_list):
					boom_points += 1
			elif i == total_points -1:
				p_list = points[:total_points-1]
				if self.whetherDistanceAllEqual(tmp, p_list):
					boom_points += 1
			else:
				p_list = points[:i] + points[i+1:]
				if self.whetherDistanceAllEqual(tmp, p_list):
					boom_points += 1
		return boom_points * self.jie_cheng(total_points-1)
			


	def getDistance(self, a, b):
		return math.sqrt(math.pow((a[0]-b[0]), 2) + math.pow((a[1]-b[1]), 2))

	def whetherDistanceAllEqual(self, p, p_list):
		all_distance = []
		for point in p_list:
			all_distance.append(self.getDistance(p, point))
		for i in range(len(all_distance) - 1):
			if all_distance[i] != all_distance[i+1]:
				return False
		return True

	def jie_cheng(self, number):
		result = 1
		while number:
			result *= number
			number -= 1
		return result


# Corret answer
class Solution(object):
	def numberOfBoomerangs(self, points):
		"""
		:type points: List[List[int]]
		:rtype: int
		"""
		results = 0
		for p in points:
			distance_map = {}
			for q in points:
				square_distance = math.pow((p[0]-q[0]), 2) + math.pow((p[1]-q[1]), 2)
				distance_map[square_distance] = 1 + distance_map.get(square_distance, 0)
			for k in distance_map:
				results += distance_map[k] * (distance_map[k] - 1)
		return results

