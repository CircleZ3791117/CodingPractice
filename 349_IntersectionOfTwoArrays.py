#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''

class Solution(object):
	def intersection(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		if len(nums1)==0 or len(nums2)==0:
			return []
		return [i for i in set(nums1) if i in set(nums2)]

'''
Solution using &
'''
class Solution(object):
	def intersection(self, nums1, nums2):
		return list(set(nums1) & set(nums2))