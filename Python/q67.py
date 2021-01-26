import numpy as np


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return bin(a+b)[2:]

s = Solution()
a = "1010"
b = "1011"
print(s.addBinary(a, b))