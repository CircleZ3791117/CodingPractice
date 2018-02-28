#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.
'''

class Solution:
	def getSum(self, a, b):
		"""
		:type a: int
		:type b: int
		:rtype: int
		"""
		# get the binary code of a and b, and then reverse binary code
		if (a >= 0 and b>= 0) or (a < 0 and b < 0):
			new_a, new_b = abs(a), abs(b)  
			re_bin_a = list(bin(new_a)[2:][::-1])
			re_bin_b = list(bin(new_b)[2:][::-1])
			size = max(len(re_bin_a), len(re_bin_b))
			if len(re_bin_a) > len(re_bin_b):
				re_bin_b.extend(['0']*(len(re_bin_a) - len(re_bin_b)))
			else:
				re_bin_a.extend(['0']*(len(re_bin_b) - len(re_bin_a)))
			print('re_bin_a:{}, re_bin_b:{}'.format(re_bin_a, re_bin_b))
			result = []
			tmp = '0'
			for i in range(size):
				if tmp == '0' and (re_bin_a[i] == '0' and re_bin_b[i] == '0'):
					result.append('0')
					print('1.result.append(0)')
					tmp = '0'
					continue
				if tmp == '0' and ((re_bin_a[i] == '1' and re_bin_b[i] == '0') or (re_bin_a[i] == '0' and re_bin_b[i] == '1')):
					result.append('1')
					print('2.result.append(1)')
					tmp = '0'
					continue
				if tmp == '0' and (re_bin_a[i] == '1' and re_bin_b[i] == '1'):
					result.append('0')
					print('3.result.append(0)')
					tmp = '1'
					continue
				if tmp == '1' and (re_bin_a[i] == '0' and re_bin_b[i] == '0'):
					result.append('1')
					print('4.result.append(1)')
					tmp = '0'
					continue
				if tmp == '1' and ((re_bin_a[i] == '1' and re_bin_b[i] == '0') or (re_bin_a[i] == '0' and re_bin_b[i] == '1')):
					result.append('0')
					print('5.result.append(0)')
					tmp = '1'
					continue
				if tmp == '1' and (re_bin_a[i] == '1' and re_bin_b[i] == '1'):
					result.append('1')
					print('6.result.append(1)')
					tmp = '1'
					continue
			if tmp == '1':
				result.append(tmp)
			print(result)
			new_result = ''.join(result[::-1])
			print('new_result is : {}'.format(new_result))
			final_result = int(new_result, 2)
			if a >= 0:
				return final_result
			else:
				return (-1) * final_result
		else:
			if a > b:
				return a-abs(b)
			else:
				return b-abs(a)




# test
s = Solution()
print(s.getSum(1, -1))

'''
Better Solution: Bit manipulation
'''
class Solution:
	def getSum(self, a, b):
		# if b == 0:
		# 	return a
		# sum_with_no_carry = a ^ b
		# carry = (a & b) << 1
		# return self.getSum(sum_with_no_carry, carry)
		# 32 bits integer max
		MAX = 0x7FFFFFFF
		# 32 bits integer min
		MIN = 0x80000000
		# MASK to get last 32 bits
		MASK = 0xFFFFFFFF
		while(b!=0):
			# ^ get different bits and & gets double 1s, << moves  carry
			a, b = ((a ^ b) & MASK), (((a & b) << 1) & MASK)
		return a if a < MAX else ~(a ^ MASK)





