#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

'''
 Solution
'''

# Method 1: Using Hash_Table:

class Solution(object):
	def singleNumber(self, nums):
		htable = {}
		for num in nums:
			try:
				htable.pop(num)
			except:
				htable[num] = 1
		return htable.popitem()[0]

'''
Time complexity: O(n). Time complexity of for loop is O(n). Time complexity of hash table(dictionary in python) operation pop is O(1).
Space complexity: O(m). The space required by hash_table is equal to the number of elements in nums.
'''

# Method 2: Using mathematics: 2*(a+b+single)-(a+a+b+b+single) = single

class Solution(object):
	def singleNumber(self, nums):
		return sum(set(nums))*2 - sum(nums)

'''
Time complexity: O(n+n) = O(n). sum will call next to iterate through nums. We can see it as sum(list(i, for i in nums)) which means the time complexity is O(n) because of the number of elements(n) in nums.
Space complexity: O(m+m) = O(m). set needs space for the elements in nums
'''

# Method 3: Using XOR: a ^ 0 = a , a ^ a = 0, (a^b)^a = (a^a)^b 

class Solution(object):
	def singleNumber(self, nums):
		sum = 0
		for num in nums:
			sum ^= numß
		return sum

'''
Time complexity: O(n)
Space complexity: O(1)
'''
