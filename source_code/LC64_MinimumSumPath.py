#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution:
    def minPathSum(self, grid: list) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return 0
        # define dp matrix
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        j = 1
        while j < n:
            dp[0][j] = dp[0][j-1] + grid[0][j]
            j += 1
        i = 1
        while i < m:
            dp[i][0] = dp[i-1][0] + grid[i][0]
            i += 1
        i = 1
        while i < m:
            j = 1
            while j < n:
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                j += 1
            i += 1
        return dp[m-1][n-1]

