# -*- coding: utf-8 -*-

"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class Solution:
    def numSquares(self, n):
        """
        Return the number of perfect square numbers which can be summed to target number.

        Args:
            n: int, target number.

        Returns:
            int, number of perfect square number.

        """
        # Generate perfect square numbers smaller than n.
        perfect_square_numbers = []
        i = 1
        square_i = i * i
        while square_i <= n:
            perfect_square_numbers.append(square_i)
            i += 1
            square_i = i * i

        cur_level = [n]
        count = 0
        while cur_level:
            count += 1
            tmp = []
            for num in cur_level:
                for val in perfect_square_numbers:
                    if num == val:
                        return count
                    if val < num:
                        tmp.append(num - val)
                    if val > num:
                        break
            cur_level = tmp
        return count
