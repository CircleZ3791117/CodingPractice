#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''

class Solution(object):
	def twoSum(self, numbers, target):
		"""
		:type numbers: List[int]
		:type target: int
		:rtype: List[int]
		"""
		result = []
		visited_map = {}
		for i in range(len(numbers) - 1):
			if visited_map.has_key(numbers[i]):
				continue
			another = target - numbers[i]
			if another in numbers[i+1:]:
				result.append(i+1)
				result.append(numbers[i+1:].index(another)+ 1 + i + 1)
				return result
			visited_map[numbers[i]] = 1
