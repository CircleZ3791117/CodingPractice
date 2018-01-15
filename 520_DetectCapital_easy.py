# !/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''

'''
Solution:
'''
class Solution:
	def detectCapitalUse(self, word):
		"""
		:type word: str
		:rtype: bool
		"""
		if all(97 <= ord(c) <= 122 for c in word): return True
		if all(65 <= ord(c) <= 90 for c in word): return True
		if 65 <= ord(word[0]) <= 90 and all(97 <= ord(c) <= 122 for c in word[1:]): return True
		return False


'''
Better Solution: use built-in function
'''
class Solution:
	def detectCapitalUse(self, word):
		return word.islower() or word.isupper() or word.istitle()