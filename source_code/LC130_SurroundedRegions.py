# -*- coding: utf-8 -*-

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""


class Solution(object):
    def solve(self, board: list) -> None:
        """
        Using DFS(Recursive traversal).

          Traverse all the node recursively on the boarder of the board. If the node value is 'O', change all the node
          within the same region to 'S'. And then change the other node to X. At last change 'S' node back to 'O'.

        Args:
            board: list(list(str)), like GO chessboard.

        Returns:
            list(list(str)), modified board
        """
        m = len(board)  # 0 axis
        if not m:
            return
        n = len(board[0])  # 1 axis
        if not n:
            return
        i, j = 0, 0
        while i < m:
            self.check_recur(i, 0, board, m, n)
            if n > 1:
                self.check_recur(i, n-1, board, m, n)
            i += 1
        while j < n:
            self.check_recur(0, j, board, m, n)
            if m > 1:
                self.check_recur(m-1, j, board, m, n)
            j += 1

        # Change board after checking recursively on the board to eat all of the 'O' that can't reach the boarder
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'

        # Returned the changed board
        return board

    def check_recur(self, i, j, board, m, n):
        if board[i][j] == 'O':
            board[i][j] = 'S'
            if i-1 >= 0:
                self.check_recur(i-1, j, board, m, n)
            if i+1 < m:
                self.check_recur(i+1, j, board, m, n)
            if j-1 >= 0:
                self.check_recur(i, j-1, board, m, n)
            if j+1 < n:
                self.check_recur(i, j+1, board, m, n)


