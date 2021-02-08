import collections
from typing import List
class GNode:
    def __init__(self):
        self.inDegree = 0
        self.neighbors = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        totalEdge = 0
        adjTable = collections.defaultdict(GNode)
        for start, end in prerequisites:
            adjTable[start].neighbors.append(end)
            adjTable[end].inDegree+=1
            totalEdge+=1

        next0Degree = collections.deque()
        for ind in adjTable:
            if adjTable[ind].inDegree == 0:
                next0Degree.append(adjTable[ind])
        removedEdge = 0
        while next0Degree:
            node = next0Degree.pop()
            for ind in node.neighbors:
                adjTable[ind].inDegree-=1
                if adjTable[ind].inDegree == 0:
                    next0Degree.append(adjTable[ind])
                removedEdge+=1
        if removedEdge == totalEdge:
            return True
        else:
            return False

numCourses = 2
prerequisites = [[1,0],[0,1]]
numCourses = 20
prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
s = Solution()
print(s.canFinish(numCourses, prerequisites))
exit(0)



