class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s.isspace():
            return 0
        words = s.split(' ')
        words = list(filter(lambda a: a != "", words))
        return len(words[-1])

s = Solution()
stt =  "Today is a nice day"
print(s.lengthOfLastWord(stt))