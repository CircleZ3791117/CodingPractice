#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

'''
Solution
'''
class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		num_count = collections.Counter(nums)
		# for k, v in num_count.iteritems():
		# 	if v > len(nums) // 2:
		# 		return 
		# Better way of writing the above 3 lines
		return max(num_count.keys(), key=num_count.get)

'''
// is the floored-division operator in Python. The result will be easily noticeable if you try dividing floating point values

# Python 2
>>> 10.0 / 3
3.3333333333333335
>>> 10.0 // 3
3.0
In Python2, dividing two ints uses integer division, which ends up getting you the same thing as floored division. However, you can still use // to get a floored result of floating point division. In Python3, dividing two ints results in a float, but using // acts as integer division.

# Python3
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
'''

'''
Solution using sort()
'''
class Solution(object):
	def majorityElement(self, nums):
		nums.sort()
		# nums.sort() return 'NoneType', so don't use nums = nums.sort()
		return nums[len(nums)//2]
		