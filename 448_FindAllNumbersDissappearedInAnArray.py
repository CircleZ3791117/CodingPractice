#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'


'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

'''
Solution
'''
class Solution:
	def findDissappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'


'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

'''
Solution
'''
class Solution:
	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		length = len(nums)
		num_map = {}
		result = []
		for i in nums:
			if not num_map.has_key(i):
				num_map[i] = 1
		for j in xrange(1, length+1):
			if not num_map.has_key(j):
				result.append(j)
		return result










