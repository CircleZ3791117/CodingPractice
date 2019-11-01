#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "CZ"

"""
Description:

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

# 将所有单调递增子区间累加起来，单调递减区间赋值为0
class Solution:
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		max_cur = 0
		asc_area = 0
		i = 1
		while i < len(prices):
			max_cur = max(0, prices[i] - prices[i-1])
			asc_area += max_cur
			i += 1
		return asc_area

# 坡峰坡谷计算法
class Solution:
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		cur_valley = prices[0]
		cur_peak = prices[0]
		i = 0
		total_profit = 0
		while i < len(prices) - 1:
			while i < len(prices) - 1 and prices[i] >= prices[i+1]:
				i += 1
			cur_valley = prices[i]
			while i < len(prices) - 1 and prices[i] <= prices[i+1]:
				i += 1
			cur_peak = prices[i]
			total_profit += cur_peak - cur_valley
		return total_profit

