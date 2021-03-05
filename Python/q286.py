import collections
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i,j, 0))
        while(queue):
            (i, j, d) = queue.popleft()
            rooms[i][j] = min(rooms[i][j], d)
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for row,col in directions:
                if i+row >=0 and i+row<len(rooms) and j+col>=0 and j+col<len(rooms[0]) and rooms[i+row][j+col]>d+1:
                    queue.append((i+row, j+col, d+1))

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
s = Solution()
s.wallsAndGates(rooms)
print(rooms)
