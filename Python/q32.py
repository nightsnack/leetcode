# 32. Longest Valid Parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for x in range(len(s))]
        max = 0
        for i in range(1, len(s)):
            if s[i] == ')' and s[i-1] == '(':
                dp[i] = ( dp[i-2] if i-2 >=0 else 0) +2
            elif s[i] == ')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1] == '(':
                if i-dp[i-1]-2 >=0:
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2] +2
                else:
                    dp[i] = dp[i - 1] + 2
            max = dp[i] if dp[i]>max else max
        return max


s = Solution
stttr = '()((()))('
stttr = ')()())'
stttr = "()(())"
print(s.longestValidParentheses(s, stttr))
exit(0)