#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "circlezhou"

'''
Description:
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
'''

class Solution(object):
	def imageSmoother(self, M):
		"""
		:type M: List[List[int]]
		:rtype: List[List[int]]
		"""
		results = []
		l = len(M)
		w = len(M[0])
		for i in range(l):
			for j in range(w):
				count = 0
				num_sum = 0
				# line above
				if i-1 >= 0:
					num_sum += M[i-1][j]
					count += 1
					if j-1 >= 0:
						num_sum += M[i-1][j-1]
						count += 1
					if j+1 < w:
						num_sum += M[i-1][j+1]
						count += 1
				# line below
				if i+1 < l:
					num_sum += M[i+1][j]
					count += 1
					if j-1 >= 0:
						num_sum += M[i+1][j-1]
						count += 1
					if j+1 < w:
						num_sum += M[i+1][j+1]
						count += 1
				# this line
				if j-1 >= 0:
					num_sum += M[i][j-1]
					count += 1
				if j+1 < w :
					num_sum += M[i][j+1]
					count += 1
				num_sum += M[i][j]
				count += 1
				ave = num_sum / count
				results.append(ave)
		while(results):
			for i in range(l):
				for j in range(w):
					M[i][j] = results.pop(0)

		return M

# Shorter answer
class Solution(object):
	def imageSmoother(self, M):
		R, C = len(M), len(M[0])
		ans = [[0] * C for _ in range(R)]

		for r in range(R):
			for c in range(C):
				nums_sum = 0
				count = 0
				for nr in [r-1, r, r+1]:
					for nc in [c-1, c, c+1]:
						if 0 <= nr < R and 0 <= nc < C:
							nums_sum += M[nr][nc]
							count += 1
				ave = nums_sum / count
				ans[r][c] = ave
		return ans


