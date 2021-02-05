import collections
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(i, j):
            if i<0 or j<0 or i>=m or j>=n:
                return
            if board[i][j]!='O':
                return
            board[i][j] = 'E'
            surr = [(0,1),(0,-1),(1,0),(-1,0)]

            for (x, y) in surr:
                dfs(x,y)

        for i in [0,m-1]:
            for j in range(0, n):
                dfs(i,j)

        for j in [0, n-1]:
            for i in range(1, m-1):
                dfs(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'



