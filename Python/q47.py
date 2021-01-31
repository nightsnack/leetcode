from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.path = []
        nums.sort()

        def backtracking():
            if len(nums) == 0:
                self.res.append(self.path.copy())
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                n = nums.pop(i)
                self.path.append(n)
                backtracking()
                self.path.pop()
                nums.insert(i, n)

        backtracking()
        return self.res

s = Solution()
nums = [1,1,2]
print(s.permuteUnique(nums))
exit(0)