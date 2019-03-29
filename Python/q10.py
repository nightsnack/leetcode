# Regular Expression Matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl = len(s)+1
        pl = len(p)+1
        dp = [[0]*(pl) for t in range(sl)]
        dp[0][0] = 1
        # for i in range(1, len(s)):
        #     dp[i][0] = 1
        for i in range (1,len(p)):
            if p[i] == '*' and dp[0][i-1] == 1:
                dp[0][i+1] = 1
        for i in range(1,sl):
            for j in range (1,pl):
                if (s[i-1] == p[j-1] or p[j-1] == '.' ):
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] == '*':
                    if (s[i-1]!=p[j-2] and p[j-2] != '.'):
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-1]or dp[i-1][j] or dp[i][j-2]


        return True if dp[len(s)][len(p)] == 1 else False

s = Solution;
print(s.isMatch(s,'ppi','p*'))