#!/usr/local/bin python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

'''

class Solution(object):
	def findShortestSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums_map = {}
		for num in nums:
			if num not in nums_map:
				nums_map[num] = 1
			else:
				nums_map[num] += 1
		degree = max(nums_map.itervalues())
		degree_num = []
		for k,v in nums_map.iteritems():
			if v == degree:
				degree_num.append(k)
		shortest_len = len(nums)
		for dnum in degree_num:
			index_list = []
			for i in range(len(nums)):
				if nums[i] == dnum:
					index_list.append(i)
			dnum_length = index_list[-1] - index_list[0] + 1
			if dnum_length < shortest_len:
				shortest_len = dnum_length
		return shortest_len


# Same logic but better code presentation
class Solution(object):
	def findShortestSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		left, right, count = {}, {}, {}
		for i,v in enumerate(nums):
			if v not in left: left[v] = i
			right[v] = i
			count[v] = count.get(v, 0) + 1
		degree = max(count.itervalues())
		ans = len(nums)
		for k, v in count.iteritems():
			if v == degree:
				ans = min(ans, right[k] - left[k] + 1)
		return ans  


