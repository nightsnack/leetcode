from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count  = 0
        def dfs(i,j):
            if i<0 or j <0 or i>m-1 or j> n-1:
                return 0
            if grid[i][j]!= '1':
                return 0
            grid[i][j] = '2'
            for x,y in [(0,1),(0,-1), (-1,0), (1,0)]:
                dfs(i+x, j+y)
            return 1

        # from itertools import product
        # borders = list(product(range(m), [0, n - 1])) \
        #           + list(product([0, m - 1], range(n)))
        #
        # for row,col in borders:
        #     if dfs(row, col):
        #         count+=1

        for i in range(m):
            for j in range(n):
                if dfs(i, j):
                    count += 1
        return count

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
s = Solution()
print(s.numIslands(grid))
exit(0)