# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*n
        dp[0] = 1
        if n ==1:
            return dp[n-1]
        dp[1] = 2
        if n <=2:
            return dp[n-1]
        for i in range(2, n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n-1]


s = Solution
print(s.climbStairs(s, 5))
exit(0)
