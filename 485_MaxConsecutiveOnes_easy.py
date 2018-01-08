# !/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Description:
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''

'''
Solution [Time Limit Exceeded]
'''
class Solution:
	def findMaxConsecutiveOnes(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 1 and nums[0] == 1:
			return 1
		max, tmp = (0, 0)
		for i in range(len(nums)):
			if nums[i] == 1:
				tmp = 1
				while(i < len(nums)-1 and nums[i+1] == 1):
					tmp += 1
					i += 1
				if tmp > max:
					max = tmp
				tmp = 0
		print(max)
		return max

'''
Solution
'''
class Solution:
	def findMaxConsecutiveOnes(self, nums):
		max = 0
		tmp = 0
		for num in nums:
			if num == 1:
				tmp += 1
			if num == 0:
				if tmp > max:
					max = tmp
				tmp = 0
		if tmp > max:
			return tmp
		return max

'''
Better Solution
'''
class Solution:
	def findMaxConsecutiveOnes(self, nums):
		maxnum = 0
		tmp = 0
		for num in nums:
			if num == 1:
				tmp += 1
				maxnum = max(tmp, maxnum)
			if num == 0:
				tmp = 0
		return maxnum



