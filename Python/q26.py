# 26. Remove Duplicates from Sorted Array
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 1
        while (1):
            k=j
            while(k<len(nums)):
                if nums[k] > nums[i-1] :
                    j = k
                    if i != j:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                    i = i + 1
                    j = j + 1
                    break
                k = k+1
            if k==len(nums):
                break
        return i


s = Solution
# nums = [0,0,0,1,1,2,3,3,3,4,4,4,5,5]
# nums = [0,1,3,4,4,6,7,7]
nums = [0,1,1]
print(s.removeDuplicates(s,nums))
print(nums)