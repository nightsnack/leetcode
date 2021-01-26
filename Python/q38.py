# 38. Count and Say
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        last = self.countAndSay(n-1)+" "
        count = 1
        current = ''
        for i in range(1, len(last)):
            if last[i] == last[i-1]:
                count = count+1
            else:
                current=current+str(count)+last[i-1]
                count = 1
        return current

s = Solution()
print(s.countAndSay(4))
exit(0)
