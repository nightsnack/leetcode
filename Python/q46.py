from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.path = []

        def backtracking():
            if len(nums)==0:
                self.res.append(self.path.copy())
                return

            for i in range(len(nums)):
                n = nums.pop(i)
                self.path.append(n)
                backtracking()
                self.path.pop()
                nums.insert(i, n)
        backtracking()
        return self.res

s = Solution()
nums = [0,1]
print(s.permute(nums))
exit(0)
