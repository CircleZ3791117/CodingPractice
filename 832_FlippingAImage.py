#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:

Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
'''

class Solution(object):
	def flipAndInvertImage(self, A):
		"""
		:type A: List[List[int]]
		:rtype: List[List[int]]
		"""
		for i in range(len(A)):
			for j in range(len(A[i])):
				self.reverse_list(A[i])
				if A[i][j] == 0:
					A[i][j] = 1
				elif A[i][j] == 1:
					A[i][j] = 0
		return A

	def reverse_list(self, l):
		tl = len(l)
		mid = tl / 2 -1
		mid = tl / 2
		for i in range(mid + 1):
			tmp = l[i]
			l[i] = l[tl-i-1]
			l[tl-i] = tmp


# Better solution using l[~i] which stands for the symmetrical position of i in the list

class Solution(object):
	def flipAndInvertImage(self, A):
		mid =  (len(A) + 1) / 2
		for row in A:
			for i in range(mid+1):
				row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
		return A



