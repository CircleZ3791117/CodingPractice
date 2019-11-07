"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


# Brute force: Returns TLE
class Solution:
    def is_valid(self, subs):
        stack = []
        i = 0
        while i < len(subs):
            if subs[i] == '(':
                stack.append(subs[i])
            elif len(stack) != 0 and stack[-1] == '(':
                stack.pop(-1)
            else:
                return False
            i += 1
        return len(stack) == 0

    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        i = 0
        j = i + 2
        while i < len(s) - 1:
            while j < len(s) + 1:
                if self.is_valid(s[i:j]):
                    cur_len = j - i
                    max_len = max(cur_len, max_len)
                j += 2
            i += 1
            j = i + 2
        return max_len


# Dynamic Programming
class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        dp = [0] * len(s)
        i = 1
        while i < len(s):
            if s[i] == ')' and s[i-1] == '(':
                if i - 2 >= 0:
                    dp[i] = dp[i-2] + 2
                else:
                    dp[i] = 2
            if s[i] == ')' and s[i-1] == ')':
                former = i - dp[i-1] - 1
                former_dp = i - dp[i-1] - 2
                if former >= 0 and s[former] == '(':
                    if former_dp >= 0:
                        dp[i] = dp[i-1] + 2 + dp[former_dp]
                    else:
                        dp[i] = dp[i-1] + 2
            i += 1
        return max(dp)

# Using Stack
class Solution3:
    def longestValidParentheses(self, s:str) -> int:
        if len(s) < 2:
            return 0
        max_len = 0
        stack = [-1]
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(i)
            elif stack[-1] != -1 and s[stack[-1]] == '(':
                stack.pop(-1)
                cur_len = i - stack[-1]
                max_len = max(max_len, cur_len)
            else:
                stack.append(i)
            i += 1
        return max_len


# Traverse from both side
class Solution4:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        left, right = 0, 0
        # traverse from left to right
        i = 0
        max_lr = 0
        while i < len(s):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_lr = max(right, max_lr)
            if right > left:
                left = 0
                right = 0
            i += 1
        # traver form right to left
        j = len(s) - 1
        left, right = 0, 0
        max_rl = 0
        while j >= 0:
            if s[j] == ')':
                right += 1
            else:
                left += 1
            if right == left:
                max_rl = max(left, max_rl)
            if left > right:
                left = 0
                right = 0
            j -= 1
        return 2 * max(max_lr, max_rl)


