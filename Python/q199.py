import collections
from typing import List

from Python.q0tree import TreeNode, stringToTreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                tree_node = queue.popleft()
                if i == (level_length-1):
                    res.append(tree_node.val)
                if tree_node.left:
                    queue.append(tree_node.left)
                if tree_node.right:
                    queue.append(tree_node.right)
        return res

s = Solution()
root = stringToTreeNode('[1,2,3,null,5,null,4]')
print(s.rightSideView(root))
exit(0)
