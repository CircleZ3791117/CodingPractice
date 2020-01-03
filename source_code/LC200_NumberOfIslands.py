# -*- coding: utf-8 -*-

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution(object):
    def numIslands(self, grid):
        """
        Return the number of Islands in a grid.

        Args:
            grid: list(list(str)), the map consists of '1' and '0', '1' stands for water, '0' stands for water.

        Returns:
            int, number of seperated islands.
        """

        if not any(grid):
            return 0

        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    #self.bfs(i, j, grid, m, n)
                    self.dfs(grid, i, j, m, n)
                    count += 1
        return count

    def bfs(self, i, j, grid, m, n):
        queue = [(i, j)]
        while queue:
            head = queue.pop(0)
            grid[head[0]][head[1]] = 'v'
            # up
            if head[0] - 1 >= 0 and grid[head[0] - 1][head[1]] == '1':
                grid[head[0] - 1][head[1]] = 'v'
                queue.append((head[0] - 1, head[1]))
            # down
            if head[0] + 1 < m and grid[head[0] + 1][head[1]] == '1':
                grid[head[0] + 1][head[1]] = 'v'
                queue.append((head[0] + 1, head[1]))
            # left
            if head[1] - 1 >= 0 and grid[head[0]][head[1] - 1] == '1':
                grid[head[0]][head[1] - 1] = 'v'
                queue.append((head[0], head[1] - 1))
            # right
            if head[1] + 1 < n and grid[head[0]][head[1] + 1] == '1':
                grid[head[0]][head[1] + 1] = 'v'
                queue.append((head[0], head[1] + 1))

    def dfs(self, grid, i, j, m, n):
        grid[i][j] = 'v'
        # up
        if i - 1 >= 0 and grid[i-1][j] == '1':
            self.dfs(grid, i-1, j, m, n)
        # down
        if i + 1 < m and grid[i+1][j] == '1':
            self.dfs(grid, i+1, j, m, n)
        # left
        if j - 1 >= 0 and grid[i][j-1] == '1':
            self.dfs(grid, i, j-1, m, n)
        # right
        if j + 1 < n and grid[i][j+1] == '1':
            self.dfs(grid, i, j+1, m, n)