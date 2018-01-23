#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
        	return
      	i = 0
      	l = len(nums)
        while(i < l):		# when you have to deal with index of array, use while, not for
        	if nums[i] == 0:
        		nums.append(nums.pop(i))
        		i -= 1
        		l -= 1
        	i += 1
        		
# Wrong method
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
        	return
      	for i in xrange(len(nums)):
      		if nums[i] == 0:
      			nums.append(nums.pop(i))
      			i -= 1	# making no sense

# test
s = Solution()
print(s.moveZeroes([0,0,1]))

# Another method
class Solution:
	def moveZeroes(self, nums):
		zero = 0
		for i in xrange(len(nums)):
			if nums[i] != 0:
				nums[zero], nums[i] = nums[i], nums[zero]
				zero += 1
