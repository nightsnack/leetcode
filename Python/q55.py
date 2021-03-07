from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == [0]:
            return True
        def recursion(position):
            if position == len(nums)-1:
                return True
            fuJump = min(position+nums[position],len(nums)-1)
            for i in range(fuJump, position, -1):
                if recursion(i):
                    return True
            return False

        return recursion(0)
nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
s = Solution()
print(s.canJump(nums))
exit(0)

