#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		"""
		:type ransomNote: str
		:type magazine: str
		:rtype: bool
		"""
		ransomNoteMap = {}
		magazineMap = {}
		ransomNoteMap = self.buildMap(ransomNote)
		magazineMap = self.buildMap(magazine)
		for k in ransomNoteMap.keys():
			if k not in magazineMap.keys():
				return False
			elif ransomNoteMap[k] > magazineMap[k]:
				return False
		return True

	def buildMap(self, s):
		result = {}
		for i in s:
			if i not in result:
				result[i] = 1
			else:
				result[i] += 1
		return result 

# Using collections
class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		return not collections.Counter(ransomNote) - collections.Counter(magazine)
