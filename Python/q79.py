from typing import List

import numpy as np


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.chessboard = np.ones((m,n), dtype= bool)
        self.res = False

        def backtracking(row, col, pos):
            if pos == len(word):
                self.res = True
                return 0
            for (i,j) in [(row+1,col), (row, col+1), (row-1, col), (row, col-1)]:
                if i>=0 and i <m and j >=0 and j<n and board[i][j] == word[pos] and self.chessboard[i][j]:
                    self.chessboard[i][j] = False
                    status = backtracking(i,j, pos+1)
                    if status == 0:
                        return 0
                    self.chessboard[i][j] = True
            return -1

        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    self.chessboard[x][y] = False
                    backtracking(x, y, 1)
                    self.chessboard[x][y] = True
        return self.res

s = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(s.exist(board,word))
exit(0)
