#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
'''
'''
Solution: [TIME LIMITTED ERROR]
'''
class Solution:
	def countBinarySubstrings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		count = 0
		for i, c in enumerate(s):
			if i == len(s)-1:
				break
			j = i+1
			step1 = 0
			while(j < len(s) and s[j] == c):
				step1 += 1
				j += 1
			if j + step1 < len(s):
				result = sum(int(i) for i in s[j:j+step1+1])
				if result == 0 or result == step1+1:
					count += 1
			#print('c:{},i:{},count:{}'.format(c, i, count)
		return count

# test 10101
s = Solution()
result = s.countBinarySubstrings('10110')
print(result)

'''
Better Solution
'''

# Using Groups
'''
Intuition

We can convert the string s into an array groups that represents the length of same-character contiguous blocks within the string. For example, if s = "110001111000000", then groups = [2, 3, 4, 6].

For every binary string of the form '0' * k + '1' * k or '1' * k + '0' * k, the middle of this string must occur between two groups.

Let's try to count the number of valid binary strings between groups[i] and groups[i+1]. If we have groups[i] = 2, groups[i+1] = 3, then it represents either "00111" or "11000". We clearly can make min(groups[i], groups[i+1]) valid binary strings within this string. Because the binary digits to the left or right of this string must change at the boundary, our answer can never be larger.

Algorithm

Let's create groups as defined above. The first element of s belongs in it's own group. From then on, each element either doesn't match the previous element, so that it starts a new group of size 1; or it does match, so that the size of the most recent group increases by 1.

Afterwards, we will take the sum of min(groups[i-1], groups[i]).
'''
class Solution:
	def countBinarySubstrings(self, s):
		result = 0
		groups = []
		count = 1
		for i in range(1, len(s)):
			if s[i] == s[i-1]:
				count += 1
			else:
				groups.append(count)
				count = 1
		groups.append(count)				
		print(groups)
		if len(groups) < 2:
			return 0
		for (j, v) in enumerate(groups[:-1]):
			result += min(v, groups[j+1])
		return result

s = Solution()
result = s.countBinarySubstrings('1011100')
print(result)

## Time Complexity: O(N)
## Space Complexity: O(N)

# ||   better way of counting groups
# \/

class Solution:
	def countBinarySubstrings(self, s):
		groups = [1]
		for i in xrange(1, len(s)):
			if s[i] != s[i-1]:
				groups.append(1)
			else:
				groups[-1] += 1
		ans = 0
		for i in xrange(1, len(groups)):
			ans += min(groups[i], groups[i-1])
		return ans

# ||   More elegant code
# \/
import itertools
class Solution:
	def countBinarySubstrings(self, s):
		groups = [len(list(v)) for _,v in itertools.groupby(s)]
		return sum(min(a, b) for a, b in zip(groups, groups[1:]))

# ||   Space Complexity == O(1) method
# \/

class Solution:
	def countBinarySubstrings(self, s):
		ans, pre, cur = 0, 0, 1
		for i in xrange(1, len(s)):
			if s[i] != s[i-1]:
				ans += min(cur, pre)
				pre, cur = cur, 1
			else:
				cur +=1
		return ans + min(cur, pre)
