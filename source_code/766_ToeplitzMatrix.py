#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'circlezhou'

'''
Description:

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input: matrix = [[1,2,3,4],
				 [5,1,2,3],
				 [9,5,1,2]]
Output: True
Explanation:
1234
5123
9512

In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.
Example 2:

Input: matrix = [[1,2],[2,2]]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.
Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].
'''

'''
Solution
'''
class Solution:
	def isToeplitzMatrix(self, matrix):
		"""
		:type matrix:List[List[int]]
		:rtype: bool
		"""
		m, n = len(matrix), len(matrix[0])
		#print(m, n)
		flag = True
		for x in range(m):
			for y in range(n):
				#print('x:{},y:{}'.format(x, y))
				if x == 0 or y == 0:
					tmpx, tmpy = x, y
					while tmpx+1 < m and tmpy+1 < n:
						if matrix[tmpx][tmpy] != matrix[tmpx+1][tmpy+1]:
							flag = False
							return flag
						tmpx = tmpx + 1 
						tmpy = tmpy + 1
		return flag

# test
matrix = [[11,74,0,93],[40,11,74,7]]
s = Solution()
print(s.isToeplitzMatrix(matrix))

'''
Better Solution
'''

'''
We ask what feature makes two coordinates (r1, c1) and (r2, c2) belong to the same diagonal?

It turns out two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.

This leads to the following idea: remember the value of that diagonal as groups[r-c]. If we see a mismatch, the matrix is not Toeplitz; otherwise it is.

'''
class Solution:
	def isToeplitzMatrix(self, matrix):
		rcmap = {}
		for r, row in enumerate(matrix):
			for c, val in enumerate(row):
				if r-c not in rcmap:
					rcmap[r-c] = val
				elif rcmap[r-c] != val:
					return False
		return True

'''
For each diagonal with elements in order a1,a2,a3,…,aka1,a2,a3,…,ak, we can check a1=a2,a2=a3,…,ak−1=aka1=a2,a2=a3,…,ak−1=ak. The matrix is Toeplitz if and only if all of these conditions are true for all (top-left to bottom-right) diagonals.

Every element belongs to some diagonal, and it's previous element (if it exists) is it's top-left neighbor. Thus, for the square (r, c), we only need to check r == 0 OR c == 0 OR matrix[r-1][c-1] == matrix[r][c].
'''
class Solution:
	def isToeplitzMatrix(self, matrix):
		return all( r == 0 or c == 0 or matrix[r][c] == matrix[r-1][c-1]
					for r, row in enumerate(matrix)
					for c, val in enumerate(row))

