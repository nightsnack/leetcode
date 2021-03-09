from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        def check_rotate(nums, start, end):
            if nums[start] < nums[end]:
                return 0
            while start < end:
                pivot = (start+end)//2
                if nums[pivot] > nums[pivot+1]:
                    return pivot+1
                else:
                    if nums[pivot] < nums[start]:
                        end = pivot-1
                    else:
                        start = pivot+1


        def binary_search(nums, start, end, target):
            while start<end:
                pivot = (start + end) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        end = pivot - 1
                    else:
                        start = pivot + 1
            return -1


        rotor = check_rotate(nums, 0, len(nums)-1)
        if nums[rotor] == target:
            return rotor
        if rotor == 0:
            return binary_search(nums, 0, len(nums)-1, target)

        if target < nums[0]:
            return binary_search(nums, rotor,  len(nums)-1, target)
        return binary_search(nums, 0, rotor, target)





nums = [1,3]
target = 3
s = Solution()
print(s.search(nums, target))