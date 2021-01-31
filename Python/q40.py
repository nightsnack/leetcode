from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                self.path.append(candidates[i])
                status = backtracking(i+1)
                self.path.pop()
                if status == -1:
                    break

        backtracking(0)
        return self.res

s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
candidates = [2,5,2,1,2]
target = 5
print(s.combinationSum2(candidates, target))
exit(0)
