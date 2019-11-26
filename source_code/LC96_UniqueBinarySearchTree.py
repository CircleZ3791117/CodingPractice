# -*- coding: utf-8 -*-

"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution:
    def numTrees(self, n: int) -> int:
        # define dp vector
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        i = 2
        while i < n + 1:
            j = 0
            while j < i:
                dp[i] += dp[j] * dp[i - 1 - j]
                j += 1
            i += 1
        return dp[n]
