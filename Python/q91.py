class Solution:
    def numDecodingstimeexceed(self, s: str) -> int:
        num = 0
        if s[0] == '0':
            return num
        def lookup(s, i, j):
            nonlocal num
            if j > len(s) or s[i] == '0' or int(s[i:j]) > 26:
                return
            elif j==len(s):
                num += 1
                return
            else:
                lookup(s, j, j+1)
                lookup(s, j, j+2)
        lookup(s, 0, 1)
        lookup(s, 0, 2)
        return num

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            temp = 0
            if int(s[i])<7 and s[i-1]=='2' or s[i-1] == '1':
                temp += dp[i-1]
            if s[i]!='0':
                temp += dp[i]
            dp[i+1] = temp
        return dp[len(s)]


s = Solution()
print(s.numDecodings('10'))
exit(0)