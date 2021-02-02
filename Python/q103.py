import collections
from typing import List

from Python.q0tree import TreeNode, stringToTreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            tree_node, level = queue.popleft()
            if not tree_node:
                continue
            if level%2 == 1:
                result[level].insert(0, tree_node.val)
            else:
                result[level].append(tree_node.val)
            queue.append((tree_node.left, level + 1))
            queue.append((tree_node.right, level + 1))
        return list(result.values())

s = Solution()
root = stringToTreeNode('[3,9,20,null,null,15,7]')
print(s.zigzagLevelOrder(root))
exit(0)
