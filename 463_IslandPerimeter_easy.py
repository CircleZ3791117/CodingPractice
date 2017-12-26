# !/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:

'''
class Solution:
	def islandPerimeter(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		perimeter = 0

		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 1:
					if i-1<0: perimeter += 1
					elif grid[i-1][j]==0: perimeter += 1
					if i+1>=len(grid): perimeter += 1
					elif grid[i+1][j]==0: perimeter += 1
					if j-1<0: perimeter += 1
					elif grid[i][j-1]==0: perimeter += 1
					if j+1>=len(grid[0]): perimeter += 1
					elif grid[i][j+1]==0: perimeter += 1
		return perimeter


'''
Better Solution
Key: Since there are no lakes, every pair of neighbour cells with different values is part of the perimeter (more precisely, the edge between them is). So just count the differing pairs, both horizontally and vertically (for the latter I simply transpose the grid).
'''
class Solution:
	def islandPerimeter(self, grid):
	    return sum(sum(map(operator.ne, [0] + row, row + [0])) for row in grid + map(list, zip(*grid)))

# test
import logging
import operator
logging.basicConfig(level = logging.INFO)
logging.info("zip={0}".format(zip([1,2],[3,4,5])))
logging.info("zip*={0}".format(zip(*[(1,3),(2,4)])))

logging.info("zip(*grid)={0}".format(map(list, zip(*[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))))
# => use zip(*[[] for _ in range()]) can realize matrix transpose
logging.info("grid + zip(*grid)={0}".format([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] + map(list, zip(*[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))))
logging.info("map(operator.ne, a, b)={0}".format(map(operator.ne, [0,0,1,0,0], [0,1,0,0,0])))
logging.info("sum(map(operator.ne, a, b))={0}".format(sum(map(operator.ne, [0,0,1,0,0], [0,1,0,0,0]))))