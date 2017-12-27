# !/usr/bin/env python
# -*- coding=utf-8 -*-
 
__author__ = 'circlezhou'

'''
Description:
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
'''

class Solution:
	def nextGreaterElement(self, findNums, nums):
		"""
		:type findNums: List[int]
		:type nums: List[int]
		:rtype: List[int]
		"""
		nums1_index = []
		result = []
		for item in findNums:
			for i in range(len(nums)):
				if nums[i] == item:
					nums1_index.append(i)
					break
		for index in nums1_index:
			pos = index
			if pos == len(nums) - 1:
				result.append(-1)
			else:
				for i in range(index + 1, len(nums)):
					if nums[i] > nums[index]:
						result.append(nums[i])
						break
					pos += 1
					if pos == len(nums) - 1:
						result.append(-1)
		return result

# test 
# [4,1,2]
# [1,3,4,2]
# [3,1,5,7,9,2,6]
# [1,2,3,5,6,7,9,11]
# # s = Solution()
# s.nextGreaterElement([3,1,5,7,9,2,6], [1,2,3,5,6,7,9,11])

'''
Better Solution:
Key: using stack to get pairs in which the first element is smaller than the second. And then use dict to store the pairs and find findNums in the keys, if found, means that the next greater value exist, else return -1.
'''
# [1,3,5,2,4]
# [6,5,4,3,2,1,7]
# Expected:
# [7,7,7,7,7]

class Solution:
	def nextGreaterElement(self, findNums, nums):
	    stack = []
	    pairs = {}
	    for num in nums:
	    	while len(stack) != 0 and stack[-1] < num:
	    		pairs[stack.pop()] = num
	    	stack.append(num)
	    return map(lambda x: pairs.get(x, -1), findNums)