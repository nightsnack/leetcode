# 22. Generate Parentheses
from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        self.output = []
        def seekpar(str, left, right):
            if left == right ==0:
                self.output.append(str)
                return
            if left != 0:
                seekpar(str+'(', left-1, right)
            if right!= 0 and right>left:
                seekpar(str+')', left, right-1)

        seekpar('(', n-1, n)
        return self.output

s = Solution()
print(s.generateParenthesis(3))