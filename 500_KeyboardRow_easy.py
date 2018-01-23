#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''

'''
Solution
'''
class Solution:
	def findWords(self, words):
		"""
		:type words: List[str]
		:rtype: List[str]
		"""
		KEYBOARD_LINE1 = 'QWERTYUIOPqwertyuiop'
		KEYBOARD_LINE2 = 'ASDFGHJKLasdfghjkl'
		KEYBOARD_LINE3 = 'ZXCVBNMzxcvbnm'
		results = []
		for word in words:
			count_line1, count_line2, count_line3 = (0,0,0)
			for i in word:
				if i in KEYBOARD_LINE1: count_line1 += 1
				elif i in KEYBOARD_LINE2: count_line2 += 1
				elif i in KEYBOARD_LINE3: count_line3 += 1
				else: raise ValueError('Invalid character!')
			if (count_line1, count_line2, count_line3) in [(count_line1, 0, 0),(0, count_line2, 0),(0, 0, count_line3)]:
				results.append(word)
		return results  

'''
Better Solution
Key: use set
'''
class Solution(object):
	def findWords(self, words):
		k_line1 = set('qwertyuiop')
		k_line2 = set('asdfghjkl')
		k_line3 = set('zxcvbnm')
		results = []
		for word in words:
			temp = set(word.lower())
			if temp & k_line1 == temp: results.append(word)
			if temp & k_line2 == temp: results.append(word)
			if temp & k_line3 == temp: results.append(word)
		return results

