from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        head = 0
        tail = 0
        cnt = 0
        min_len = len(s)
        res = ''
        chdict = Counter()
        for tc in t:
            chdict[tc] += 1
        while (tail < len(s)):
            c = s[tail]
            chdict[c] -= 1
            if chdict[c] >= 0:
                cnt+=1
            while (cnt == len(t)):
                if (tail - head+1 <= min_len):
                    min_len = tail - head +1
                    res = s[head:tail+1]
                chdict[s[head]]+=1
                if chdict[s[head]] > 0:
                    cnt -= 1
                head+=1
            tail+=1
        return res

s1 = Solution()
s = "abc"
t = "ac"
print(s1.minWindow(s, t))
exit(0)