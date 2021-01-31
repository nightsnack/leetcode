from typing import List

import numpy as np


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        # self.
        self.positionboard = np.ones((n,n),dtype=bool)
        self.chessboard = []

        def diagonal(row, col):
            columns = []
            rows = []
            for i in range(n):
                sub = np.abs(i-row)
                if col-sub>=0:
                    rows.append(i)
                    columns.append(col-sub)
                if col+sub<=n-1:
                    rows.append(i)
                    columns.append(col+sub)
            return rows,columns

        def backtracking(row):
            if row==n:
                sq = []
                for i in range(n):
                    rowtemplate = ['.'] * n
                    rowtemplate[self.chessboard[i]] = 'Q'
                    sq.append(''.join(rowtemplate))
                self.res.append(sq)
                return


            for j in range(n):
                if self.positionboard[row][j]:
                    self.chessboard.append(j)
                    positionbackup = self.positionboard.copy()
                    self.positionboard[row,:] = False
                    self.positionboard[:, j] = False
                    rs,cs = diagonal(row,j)
                    self.positionboard[rs,cs] = False
                    backtracking(row+1)
                    self.positionboard = positionbackup.copy()
                    self.chessboard.pop()
        backtracking(0)
        return self.res

s = Solution()
print(s.solveNQueens(8))
exit(0)