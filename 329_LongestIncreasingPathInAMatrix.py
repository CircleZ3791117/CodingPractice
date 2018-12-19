#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = circlezhou

'''
Description:

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

'''

class Solution:
	def longestIncreasingPath(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: int
		"""
		if not matrix or len(matrix) < 1 or len(maxtrix[0]) < 1:
			return 0 
		road_map = {} # record the loggest path from each node
		H = len(matrix)
		w = len(matrix[0])


	


