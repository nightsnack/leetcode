from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        square_numbers = [i**2 for i in range(int(sqrt(n))+1)]
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for sq in square_numbers:
                if sq<=n:
                    dp[i] = min(dp[i], dp[i-sq]+1)
        return int(dp[-1])

s = Solution()
print(s.numSquares(13))
exit(0)
