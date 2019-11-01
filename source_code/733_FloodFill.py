#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

'''
Description:

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
'''

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :newColor: int
        :rtype: List[List[int]]
        """
        target_coordinates_set = set()
        r_len = len(image)
        c_len = len(image[0])
        image_tag = [[0 for _ in range(c_len)] for _ in range(r_len)]
        target_coordinates_set = self.add_equal_around(image, (sr, sc), r_len, c_len, target_coordinates_set, image_tag)
        for coordinate in target_coordinates_set:
            image[coordinate[0]][coordinate[1]] = newColor
        return image

    def add_equal_around(self, image, coordinate, r, c, target_coordinates_set, image_tag):
        target_coordinates_set.add(coordinate)
        sr = coordinate[0]
        sc = coordinate[1]
        image_tag[sr][sc] = 1
        if sr - 1 >= 0 and image_tag[sr-1][sc] == 0 and image[sr - 1][sc] == image[sr][sc]:
            target_coordinates_set = self.add_equal_around(image, (sr - 1, sc), r, c, target_coordinates_set, image_tag)
        if sr + 1 < r and image_tag[sr+1][sc] == 0 and image[sr + 1][sc] == image[sr][sc]:
            target_coordinates_set = self.add_equal_around(image, (sr + 1, sc), r, c, target_coordinates_set, image_tag)
        if sc - 1 >= 0 and image_tag[sr][sc-1] == 0 and image[sr][sc - 1] == image[sr][sc]:
            target_coordinates_set = self.add_equal_around(image, (sr, sc - 1), r, c, target_coordinates_set, image_tag)
        if sc + 1 < c and image_tag[sr][sc+1] == 0 and image[sr][sc + 1] == image[sr][sc]:
            target_coordinates_set = self.add_equal_around(image, (sr, sc + 1), r, c, target_coordinates_set, image_tag)
        return target_coordinates_set

 # Store the original color and when finding the target one, just change the value of it, in this way, we don't have to matain a flag_map
class Solution(object):
 	def floodFill(self, image, sr, sc, newColor):
 		R, C, source_color = len(image), len(image[0]), image[sr][sc]
 		def dfs(r, c):
 			if not (0 <= r < R and 0 <= c < C) or image[r][c] != source_color:
 				return
 			image[r][c] = newColor
 			[dfs(r+x, c+y) for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]]
 		if image[sr][sc] != newColor:
 			dfs(sr, sc)
 		return image





