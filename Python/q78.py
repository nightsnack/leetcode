from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
        self.path = []
        # nums.sort()

        def backtracking(ind):
            for i in range(ind,len(nums)):
                self.path.append(nums[i])
                self.res.append(self.path.copy())
                backtracking(i+1)
                self.path.pop()
            return

        backtracking(0)
        return self.res

s = Solution()
nums = [1,2,3]
print(s.subsets(nums))