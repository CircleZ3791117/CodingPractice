# !/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''
class Solution(object):
	def maxAreaOfIsland(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		m = len(grid)
		n = len(grid[0])
		tag = [[0 for y in range(n)] for x in range(m)]
		max_area = 0
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1 and tag[i][j] == 0:
					current = 1
					tag[i][j] = 1
					max_area = max(max_area, self.get_area(i, j, tag, grid, current))
		print('max_area: {}'.format(max_area))
		return max_area

	def get_area(self, x, y, tag, grid, current):
		if y + 1 < len(grid[0]) and grid[x][y+1] == 1 and tag[x][y+1] == 0:
			current += 1
			print('to right({},{})- current:{}'.format(x, y+1, current))
			tag[x][y+1] = 1
			current = self.get_area(x, y+1, tag, grid, current)
		if x + 1 < len(grid) and grid[x+1][y] == 1 and tag[x+1][y] == 0:
			current += 1
			print('to down({},{})- current:{}'.format(x+1, y, current))
			tag[x+1][y] = 1
			current = self.get_area(x+1, y, tag, grid, current)
		if x - 1 >= 0 and grid[x-1][y] == 1 and tag[x-1][y] == 0:
			current += 1
			print('to left({},{})- current:{}'.format(x-1, y, current))
			tag[x-1][y] = 1
			current = self.get_area(x-1, y, tag, grid, current)
		if y - 1 >= 0 and grid[x][y-1] == 1 and tag[x][y-1] == 0:
			current += 1
			print('to up({},{})- current:{}'.format(x, y-1, current))
			tag[x][y-1] = 1
			current = self.get_area(x, y-1, tag, grid, current)
		return current


# test 
# s = Solution()
# s.maxAreaOfIsland([[1,1,0,0,1],
# 					[1,1,0,0,1],
# 					[0,1,0,1,1],
# 					[0,0,0,1,1]])

'''
Better Solution
'''
# recursive
class Solution:
	def maxAreaOfIsland(self, grid):
		m, n = len(grid), len(grid[0])
		def dfs(i, j):
			if 0 <= i < m and 0 <= j < n  and grid[i][j]:
				grid[i][j] = 0
				return 1 + dfs(i-1,j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
			else:
				return 0
		areas = [dfs(i,j) for i in range(m) for j in range(n) if grid[i][j]]
		return max(areas) if areas else 0
# iterative
class Solution:
	def maxAreaOfIsland(self, grid):
		seen = set()
		max_area = 0
		for r0 , row in enumerate(grid):
			for c0, val in enumerate(row):
				if (r0,c0) not in seen and val:
					seen.add((r0,c0))
					stack = [(r0,c0)]
					tmp = 0
					while(stack):
						r, c = stack.pop()
						tmp += 1
						for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r, c+1)):
							if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in seen:
								stack.append((nr, nc))
								seen.add((nr, nc))
					max_area = max(tmp, max_area)
		return max_area




















 













