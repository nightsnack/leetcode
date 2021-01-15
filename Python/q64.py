#64. Minimum Path Sum
from typing import List

import numpy as np


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        grid = np.array(grid, dtype=int)
        m,n = grid.shape
        dp = np.zeros((m, n), dtype=int)
        dp[0,:] = np.cumsum(grid, axis=1)[0,:]
        dp[:,0] = np.cumsum(grid, axis=0)[:,0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j])+grid[i][j]
        return dp[m-1][n-1]

s = Solution
grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[9]]
print(s.minPathSum(s, grid))
exit(0)