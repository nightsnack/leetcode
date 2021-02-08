import collections
from typing import List

class GNode:
    def __init__(self):
        self.inDegree = 0
        self.neighbors = []
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        order = collections.deque()
        totalEdge = 0
        adjTable = collections.defaultdict(GNode)
        for start, end in prerequisites:
            adjTable[start].neighbors.append(end)
            adjTable[end].inDegree += 1
            totalEdge += 1

        next0Degree = collections.deque()
        for ind in adjTable:
            if adjTable[ind].inDegree == 0:
                next0Degree.append(adjTable[ind])
                order.appendleft(ind)
        removedEdge = 0
        while next0Degree:
            node = next0Degree.pop()
            for ind in node.neighbors:
                adjTable[ind].inDegree -= 1
                if adjTable[ind].inDegree == 0:
                    next0Degree.append(adjTable[ind])
                    order.appendleft(ind)
                removedEdge += 1

        if removedEdge == totalEdge:
            if len(list(order)) != numCourses:
                for i in range(numCourses):
                    if i not in adjTable:
                        order.appendleft(i)
            return list(order)
        else:
            return []

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
s = Solution()
print(s.findOrder(numCourses, prerequisites))
exit(0)