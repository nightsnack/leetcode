# 72. Edit Distance
import numpy as np


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1)==0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)
        m = len(word2)+1
        n = len(word1)+1
        dp = np.zeros((m,n), dtype=int)
        dp[0, :] = np.array(range(0,n))
        dp[:,0] = np.array(range(0,m))
        for i in range(1,m):
            for j in range(1, n):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
        return dp[m-1][n-1]

s = Solution
word1 = "horse"
word2 = "ros"
word1 = "intention"
word2 = "execution"
print(s.minDistance(s, word1, word2))
exit(0)