# -*- coding: utf-8 -*-

"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation."""

import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list) -> list:
        """
        Return all the paths of word ladders if there exits.

        :param beginWord: str, start word
        :param endWord: str, end word
        :param wordList: list, dictionary of usable wordlist
        :return: list, list of word ladders
        """

        res = list()  # final result
        wordList = set(wordList)  # remove duplicate word
        if beginWord in wordList:
            wordList.remove(beginWord)  # remove start word. note: remove element should be in the list
        # key is end word of current list of word list, value is list of list
        layer = dict()
        # initialize
        layer[beginWord] = [[beginWord]]

        while layer:
            # for the key that not in the dict, initialize it with an empty list
            new_layer = collections.defaultdict(list)
            for word_key in layer:
                if word_key == endWord:
                    # using the list method extend to add elements to the final result straight-forward
                    res.extend(word_ladder for word_ladder in layer[word_key])
                else:
                    for i in range(len(word_key)):
                        for j in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = word_key[:i] + j + word_key[i + 1:]
                            if new_word in wordList:
                                new_layer[new_word] += [word_ladder + [new_word] for word_ladder in layer[word_key]]

            wordList -= new_layer.keys()  # remove word that already in the new_layer keys
            layer = new_layer

        return res
