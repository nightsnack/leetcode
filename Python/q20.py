class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        par = {"(":")","[":"]","{":"}"}
        stack = []
        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            elif not stack or par[stack.pop()]!=s[i]:
                return False
        if not stack:
            return True
        else:
            return False

s = Solution()
print(s.isValid(']'))
exit(0)

