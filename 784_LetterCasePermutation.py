#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string. Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length at most 12.
S will consist only of letters or digits.
'''

'''
Solution
'''
class Solution:
	def letterCasePermutation(self, S):
		"""
		:type S: str
		:rtype: List[str]
		"""
		ans = [[]]
		for letter in S:
			n = len(ans)
			if letter.isalpha():
				for i in xrange(n):
					ans.append(ans[i][:])
					ans[i].append(letter.lower())
					ans[i+n].append(letter.upper())
			else:
				for i in xrange(n):
					ans[i].append(letter)
		return map("".join, ans)

'''
Complexity Analysis

Time Complexity: O(2^N * N), where N is the length of S. This reflects the cost of writing the answer.

Space Complexity: O(2^N * N).
'''

'''
Intuition

Maintain the correct answer as we increase the size of the prefix of S we are considering.

For example, when S = "abc", maintain ans = [""], and update it to ans = ["a", "A"], ans = ["ab", "Ab", "aB", "AB"], ans = ["abc", "Abc", "aBc", "ABc", "abC", "AbC", "aBC", "ABC"] as we consider the letters "a", "b", "c".

Algorithm

If the next character c is a letter, then we will duplicate all words in our current answer, and add lowercase(c) to every word in the first half, and uppercase(c) to every word in the second half.

If instead c is a digit, we'll add it to every word.
'''





