#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'
'''
Description:

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

'''
Solution:
step: tranfrom to bits -> use a counter to calculate the number of different positions

hint: method of transform a int to binary in python
>>> bin(6)  
'0b110'

>>> bin(6)[2:]  
'110'

>>> bin(6)[2:].zfill(8)
'00000110'

>>> '{0:08b}'.format(6)
'00000110'
Just to explain the parts of the formatting string:
{} places a variable into a string
0 takes the variable at argument position 0
: adds formatting options for this variable (otherwise it would represent decimal 6)
08 formats the number to eight digits zero-padded on the left
b converts the number to its binary representation
'''
class Solution:
	def hammingDistance(self, x, y):
		"""
		:type x: int
		:type y: int
		:rtype: int
		"""
		x_binary_str = '{0:032b}'.format(x)
		y_binary_str = '{0:032b}'.format(y)
		count = 0
		for i in range(32):
			if x_binary_str[i] != y_binary_str[i]:
				count += 1
		return count

'''
better solution
'''
class Solution:
	def hammingDistance(self, x, y):
		return bin(x^y).count('1')