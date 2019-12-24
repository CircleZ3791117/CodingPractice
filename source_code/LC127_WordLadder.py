# -*- coding: utf-8 -*-

"""
Description:

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

import collections


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        Get the shortest ladder length of the path from begin word to end word using word list.

        Args:
            beginWord: str, start word.
            endWord: str, end word.
            wordList: List[str], word list.

        Returns:
            int, the shortest length of possible ladder.
        """
        wordList = set(wordList)  # Remove duplicate word
        # Remove begin word if exists in the word list
        while beginWord in wordList:
            wordList.remove(beginWord)
        layer = dict()  # key is the last word of each element(word list) to its value
        layer[beginWord] = [[beginWord]]
        result = []  # element stands for all the possible paths

        while layer:
            new_layer = collections.defaultdict(list)
            for key_word in layer:
                if key_word == endWord:
                    result.extend(k for k in layer[key_word])
                else:
                    for i in range(len(key_word)):
                        for j in "abcdefghijklmnopqrstuvwxyz":
                            new_word = key_word[:i] + j + key_word[i + 1:]
                            if new_word in wordList:
                                new_layer[new_word] += [item + [new_word] for item in layer[key_word]]
            layer = new_layer
            wordList -= new_layer.keys()

        if result:
            return len(result[0])
        else:
            return 0
