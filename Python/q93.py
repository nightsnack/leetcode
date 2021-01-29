# 93. Restore IP Addresses
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.path = []
        self.res = []
        self.input = s

        def validip(begin, end) -> bool:
            if end-begin > 1 and self.input[begin]=='0':
                return False
            ip = int(self.input[begin:end])
            if ip > 255:
                return False
            else:
                return True

        def backtracking(split, begin):
            if begin == len(self.input) and split==4:
                self.res.append('.'.join(self.path))
                return
            if len(self.input)-begin < 4-split or len(self.input) - begin > 3*(4-split):
                return

            for i in range(1,4):
                if begin+i > len(self.input):
                    break
                if validip(begin, begin+i):
                    self.path.append(self.input[begin: begin+i])
                    backtracking(split+1, begin+i)
                    self.path.pop()

        backtracking(0, 0)
        return self.res

s = Solution()
s1 = "25525511135"
print(s.restoreIpAddresses(s1))