# Definition for a binary tree node.
import numpy as np


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or root.left==None and root.right==None :
            return True
        return self.check(root.left, root.right)
    def check(self, left, right):
        if left == None and right == None:
            return True
        if (bool(left) ^ bool(right)) or left.val!= right.val:
            return False
        return self.check(left.left, right.right) and self.check( left.right, right.left)


s = Solution()
root = TreeNode(val=1, left=TreeNode(val=2,left=TreeNode(val=None), right=TreeNode(val=3)), right=TreeNode(val=2,left=TreeNode(val=None)))
root = TreeNode(val=1, left=TreeNode(val=0))
root = TreeNode(val=2, left=TreeNode(val=3,left=TreeNode(val=4), right=TreeNode(val=5)), right=TreeNode(val=3,left=TreeNode(val=5), right=None))

print(s.isSymmetric(root))