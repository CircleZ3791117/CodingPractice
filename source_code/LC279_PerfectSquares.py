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
        sn_len = len(perfect_square_numbers)

        min_num = n

        for i in range(sn_len):
            cur_seq = [[perfect_square_numbers[i]]]
            while cur_seq:
                for item in cur_seq:
                    if sum(item) == n:
                        min_num = min(min_num, len(item))
                        cur_seq = []
                        break
                    if sum(item) > n:
                        cur_seq.remove(item)

                new_seq = []

                for item in cur_seq:
                    next_item_level = [item.copy() for _ in range(sn_len)]
                    for k in range(sn_len):
                        next_item_level[k].append(perfect_square_numbers[k])
                    for new_item in next_item_level:
                        new_seq.append(new_item)
                cur_seq = new_seq

        return min_num
