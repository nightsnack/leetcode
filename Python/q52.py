import numpy as np


class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        # self.
        self.positionboard = np.ones((n, n), dtype=bool)
        self.chessboard = []

        def diagonal(row, col):
            columns = []
            rows = []
            for i in range(n):
                sub = np.abs(i - row)
                if col - sub >= 0:
                    rows.append(i)
                    columns.append(col - sub)
                if col + sub <= n - 1:
                    rows.append(i)
                    columns.append(col + sub)
            return rows, columns

        def backtracking(row):
            if row == n:
                self.res+=1
                return

            for j in range(n):
                if self.positionboard[row][j]:
                    self.chessboard.append(j)
                    positionbackup = self.positionboard.copy()
                    self.positionboard[row, :] = False
                    self.positionboard[:, j] = False
                    rs, cs = diagonal(row, j)
                    self.positionboard[rs, cs] = False
                    backtracking(row + 1)
                    self.positionboard = positionbackup.copy()
                    self.chessboard.pop()

        backtracking(0)
        return self.res

s = Solution()
print(s.totalNQueens(4))
exit(0)