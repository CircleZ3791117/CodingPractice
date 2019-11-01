#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "CZ"

"""
Description:

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""

# TLE (Time Limit Exceeded)
class Solution:
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		max_profit = 0
		i = 0
		while i < (len(prices) - 1):
			j = i + 1
			while j < len(prices):
				if prices[j] - prices[i] > max_profit:
					max_profit = prices[j] - prices[i]
				j += 1
			i += 1
		return max_profit

# From Solution
class Solution:
	def maxProfit(self, prices):
		if len(prices) > 0:
			min_val = prices[0]
			max_profit = 0
			for i in range(len(prices)):
				if prices[i] < min_val:
					min_val = prices[i]
				elif prices[i] - min_val > max_profit:
					max_profit = prices[i] - min_val
			return max_profit
		else:
			return 0

# From discuss
class Solution:
	def maxProfit(self, prices):
		max_cur = 0
		max_sofar = 0
		i = 1
		while i < len(prices):
			max_cur = max(0, max_cur + (prices[i] - prices[i-1]))
			max_sofar = max(max_cur, max_sofar)
			i += 1
		return max_sofar



