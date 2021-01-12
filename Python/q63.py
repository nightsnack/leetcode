# 63. Unique Paths II
from typing import List

import numpy as np


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        obstacleGrid = np.array(obstacleGrid)
        m,n = obstacleGrid.shape
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        dp = np.ones(obstacleGrid.shape, dtype=int)
        for i in range(0,m):
            if obstacleGrid[i][0] == 1:
                dp[i:m,0] = 0
                break
        for j in range(0, n):
            if obstacleGrid[0][j] == 1:
                dp[0,j:n] = 0
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j]=0
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m-1][n-1]

s = Solution
obstacleGrid = [[0,1,0],[0,0,1],[0,0,0]]
obstacleGrid = [[0,0],[1,1],[0,0]]
print(s.uniquePathsWithObstacles(s, obstacleGrid))
exit(0)