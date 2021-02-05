"""
# Definition for a Node.
"""
import collections


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        queue = collections.deque([node])
        visited = {}
        one = Node(node.val)
        visited[1] = one
        while(queue):
            old = queue.popleft()
            neighbor_list = []
            for old_nei in old.neighbors:
                if old_nei.val not in visited:
                    new_nei = Node(old_nei.val)
                    visited[old_nei.val] = new_nei
                    queue.append(old_nei)
                neighbor_list.append(visited[old_nei.val])
            visited[old.val].neighbors=neighbor_list
        return visited[1]


