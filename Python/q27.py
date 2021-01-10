# 27. Remove Element
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        i=0
        j = len(nums)-1
        while (i<=j):
            if nums[i] != val:
                i = i+1
            elif nums[j]== val:
                j = j-1
            else:
                nums[i] = nums[j]
                i = i+1
                j = j-1
        return i

s = Solution
nums = [0,1,2,2,3,0,4,2]
val = 2
nums = [3,2,2,3]; val = 3
nums = [0]; val = 0
# nums = [3,3,3,3]; val = 3
# nums = [2]; val = 3
# nums = [4,5]; val = 4
print(s.removeElement(s, nums, val))
print(nums)