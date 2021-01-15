#53. Maximum Subarray
from typing import List

import numpy as np


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        sum = nums[0]
        dp = np.zeros(len(nums), dtype=int)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] + nums[i] > nums[i]:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
            sum = dp[i] if dp[i] > sum else sum

        return sum

s = Solution
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-1, -2]
# nums = [1, 2]
print(s.maxSubArray(s, nums))
exit(0)
