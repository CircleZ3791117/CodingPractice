#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray(self, nums: list) -> int:
        # define dp vector
        dp = [0] * len(nums)
        dp[0] = nums[0]
        i = 1
        while i < len(dp):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
            i += 1
        return max(dp)
