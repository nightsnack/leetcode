import collections

from Python.q0tree import TreeNode, stringToTreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while (queue):
            node, level = queue.popleft()
            if not node:
                continue
            if not node.left and not node.right:
                return level
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))


s = Solution()
# root = stringToTreeNode('[3,9,20,null,null,15,7]')
root = stringToTreeNode('[2,null,3,null,4,null,5,null,6]')
root = stringToTreeNode('[3,9,20,null,null,15,7]')
print(s.minDepth(root))
exit(0)



