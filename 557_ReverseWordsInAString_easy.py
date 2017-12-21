# !/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'circlezhou'

'''
Descripiton:
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''

'''
Solution
'''
class Solution:
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		results = []
		for word in s.split(' '):
			results.append(self.reverse(word))
		return ' '.join(results)

	def reverse(self, w):
		list_w = list(w)
		for i in range(len(list_w)/2):
			temp = list_w[i]
			list_w[i] = list_w[-i-1]
			list_w[-i-1] = temp
		return ''.join(list_w)

'''
Better Solution:
Key: use shard and double reverse
'''
# Here I first reverse the order of the words and then reverse the entire string.

def reverseWords(self, s):
    return ' '.join(s.split()[::-1])[::-1]
# That's a bit shorter than the more obvious one:

def reverseWords(self, s):
    return ' '.join(x[::-1] for x in s.split())

# The double reversal is not just shorter but also faster. Trying both versions as well as the optimized obvious solution (using a list comprehension instead of a generator expression), five attempts each:

'''
>>> from timeit import timeit
>>> setup = 's = "Let\'s take LeetCode contest"'
>>> statements = ("' '.join(s.split()[::-1])[::-1]",
	          "' '.join(x[::-1] for x in s.split())",
	          "' '.join([x[::-1] for x in s.split()])")
>>> for stmt in statements:
        print ' '.join('%.2f' % timeit(stmt, setup) for _ in range(5)), 'seconds for:', stmt

0.79 0.78 0.80 0.82 0.79 seconds for: ' '.join(s.split()[::-1])[::-1]
2.10 2.14 2.08 2.06 2.13 seconds for: ' '.join(x[::-1] for x in s.split())
1.27 1.26 1.28 1.28 1.26 seconds for: ' '.join([x[::-1] for x in s.split()])
With many more words, the double reversal's advantage gets even bigger:

>>> setup = 's = "Let\'s take LeetCode contest" * 1000'
>>> for stmt in statements:
        print ' '.join('%.2f' % timeit(stmt, setup, number=1000) for _ in range(5)), 'seconds for:', stmt

0.16 0.14 0.13 0.14 0.14 seconds for: ' '.join(s.split()[::-1])[::-1]
0.69 0.71 0.69 0.70 0.70 seconds for: ' '.join(x[::-1] for x in s.split())
0.63 0.68 0.63 0.64 0.64 seconds for: ' '.join([x[::-1] for x in s.split()])
'''