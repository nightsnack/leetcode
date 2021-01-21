# 104. Maximum Depth of Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    maxdep = 0

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.preOrder(root, 1)
        return self.maxdep
    def preOrder(self, root: TreeNode, depth: int):
        if not root:
            return
        if depth>self.maxdep:
            self.maxdep = depth
        self.preOrder(root.left, depth+1)
        self.preOrder(root.right, depth+1)


s = Solution()
root = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20,left=TreeNode(val=15), right=TreeNode(val=7)))
print(s.maxDepth(root))