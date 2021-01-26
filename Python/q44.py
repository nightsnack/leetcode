# 44. Wildcard Matching
import numpy as np


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(p)
        n = len(s)
        if (m==0 and n==0):
            return True
        elif (m==0):
            return False
        dp = np.zeros((m+1, n+1),dtype=bool)
        dp[0][0] = True
        for i in range(1, m+1):
            if (p[i-1] == '*'):
                dp[i][0] = dp[i-1][0]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[j-1] == p[i-1] or p[i-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[m][n]

so = Solution()
s = "adceb"
p = "*a*b"
s = "acdcb"
p = "a*c?b"
s = "aa"
p = "a"
print(so.isMatch(s, p))
exit(0)