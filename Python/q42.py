# 42. Trapping Rain Water
from typing import List

import numpy as np


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        height = np.array(height, dtype=int)
        max = np.max(height)
        maxind = np.argmax(height)
        total = np.ones(len(height), dtype=int)*max - height
        dp = np.zeros(len(height))
        # dp[0] = height[0]
        # total[0] = total[0] - (max - height[0])
        for i in range(0, maxind):
            dp[i] = height[i] if i-1 < 0 or height[i] > dp[i-1] else dp[i-1]
            total[i] = total[i] - (max - dp[i])
        for i in range(len(height)-1, maxind, -1):
            dp[i] = height[i] if i+1>=len(height) or height[i]>dp[i+1] else dp[i+1]
            total[i] = total[i] - (max - dp[i])
        return np.sum(total)


s = Solution
height = [4,2,0,3,2,5]
print(s.trap(s, height))
exit(0)