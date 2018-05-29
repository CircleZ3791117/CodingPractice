#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

'''
class Solution(object):
    def minMoves(self, nums):
        """
        :type: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        total_moves = 0
        while not self.all_equal(nums):
            max_value = max(nums)
            min_value = min(nums)
            steps = max_value - min_value
            max_index = nums.index(max_value)
            self.add_steps_to_rest(nums, max_index, steps)
            total_moves += steps
        return total_moves

    def all_equal(self, nums):
        """Whether the element in a list are all equal to each other"""
        if max(nums) != min(nums):
            return False
        return True

    def add_steps_to_rest(self, nums, index, steps):
        """Add a specific value to elements in a list except for the max one"""
        for i in range(len(nums)):
            nums[i] += steps
        nums[index] -= steps
        return nums



