from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
        self.path = []
        nums.sort()
        def backtracking(ind):
            for i in range(ind, len(nums)):
                if i>ind and nums[i] == nums[i-1]:
                    continue
                self.path.append(nums[i])
                if self.path not in self.res:
                    self.res.append(self.path.copy())
                backtracking(i + 1)
                self.path.pop()
            return

        backtracking(0)
        return self.res

s = Solution()
nums = [1, 2, 2]
print(s.subsetsWithDup(nums))