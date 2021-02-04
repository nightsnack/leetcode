
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

import collections

from Python.q0tree import stringToTreeNode


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = collections.deque([root])
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                tree_node = queue.popleft()
                if i == (level_length-1):
                    tree_node.next = None
                else:
                    tree_node.next = queue[0]
                if tree_node.left:
                    queue.append(tree_node.left)
                if tree_node.right:
                    queue.append(tree_node.right)
        return root

s = Solution()
root = stringToTreeNode('[1,2,3,4,5,6,7]')
print(s.connect(root))
exit(0)
