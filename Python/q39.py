from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        self.path = []

        def backtracking(ind):
            sumup = sum(self.path)
            if sumup == target:
                self.res.append(self.path.copy())
                return 0
            if sumup > target or ind >= len(candidates):
                return -1

            for i in range(ind, len(candidates)):
                self.path.append(candidates[i])
                status = backtracking(i)
                self.path.pop()
                if status == -1:
                    break


        backtracking(0)
        return self.res

s = Solution()
candidates = [2,3,6,7]
target = 7
candidates = [2,3,5]
target = 8
candidates = [2]
target = 1
print(s.combinationSum(candidates, target))
exit(0)