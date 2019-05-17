#!/usr/bine/env python
# -*- coding: utf-8 -*-

"""
Description:

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		i = 0
		j = 0
		res = []
		while i < len(nums1) and j < len(nums2):
			if nums1[i] <= nums2[j]:
				res.append(nums1[i])
				i += 1
			else:
				res.append(nums2[j])
				j += 1
		if i == len(nums1):
			res.append(nums2[j:])
		if j == len(nums2)
			res.append(nums1[i:])
		rl = len(res)
		if rl == 0:
			return 0
		if rl % 2 == 0:
			return (res[rl/2] + res[rl/2-1])/2.0
		else:
			return res[rl//2]