from typing import List

import numpy as np


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_mat = np.zeros((numCourses, numCourses), dtype=bool)
        for f,t in prerequisites:
            adj_mat[f][t] = True
        visited = np.zeros(numCourses, dtype=int) # 0: not visit 1 visiting 2 finish
        self.nocircle = True
        def dfs(root):
            visited[root] = 1
            for i in range(numCourses):
                if adj_mat[root][i]:
                    if visited[i] == 1:
                        self.nocircle = False
                        break
                    elif visited[i]==0:
                        dfs(i)
            visited[root] = 2
        for i in range(numCourses):
            dfs(i)
        return self.nocircle

numCourses = 2
prerequisites = [[1,0],[0,1]]
numCourses = 20
prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
s = Solution()
print(s.canFinish(numCourses, prerequisites))
exit(0)