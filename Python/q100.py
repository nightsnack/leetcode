# 100. Same Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preorder(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if (not p or not q) or p.val!=q.val:
                return False
            if preorder(p.left, q.left) and preorder(p.right, q.right):
                return True
        return preorder(p, q)


s = Solution()
p = TreeNode(val=1, left=(TreeNode(val=2)),right=None)
q = TreeNode(val=1, left=None,right=TreeNode(val=2))
print(s.isSameTree(p,q))
exit(0)