#62. Unique Paths
import numpy as np


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = np.ones((m,n), dtype=int)
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

s = Solution
m = 3
n = 7
print(s.uniquePaths(s, m,n))
exit(0)