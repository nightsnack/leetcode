from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0]>end:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(end, intervals[i][1])
        res.append([start, end])
        return res

s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
print(s.merge(intervals))

