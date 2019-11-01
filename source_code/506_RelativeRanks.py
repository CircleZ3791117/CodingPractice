#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'circlezhou'

'''
Description:
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
'''

class Solution(object):
	def findRelativeRanks(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		sorted_nums = sorted(nums, reverse=True)
		num_map = {}
		for score in nums:
			score_rank = sorted_nums.index(score) + 1
			if score_rank == 1:
				score_rank = "Gold Medal"
			elif score_rank == 2:
				score_rank = "Silver Medal"
			elif score_rank == 3:
				score_rank = "Bronze Medal"
			else:
				score_rank = str(score_rank)
			num_map[score] = score_rank
		results = []
		# wrong way because the sequence of the hashmap is totally different from the element add sequence
		# for values in num_map.itervalues():
		# 	results.append(values)
		for num in nums:
			results.append(num_map[num])
		return results

# Simplify the process
class Solution(object):
	def findRelativeRanks(self, nums):
		rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(nums) + 1)))
		sort = sorted(nums, reverse=True)
		return list(map(dict(zip(sort, rank)).get, nums))
