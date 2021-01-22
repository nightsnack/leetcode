class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.res = False
        def preOrder( root: TreeNode, sum: int):
            if not root:
                return
            sum = sum + root.val
            if not root.left and not root.right and sum == targetSum:
                self.res = True
            preOrder(root.left, sum)
            preOrder(root.right, sum)
        preOrder(root, 0)
        return self.res
root = TreeNode(5, left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))), right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, left=None, right=TreeNode(1))))
targetSum = 13
s = Solution()
print(s.hasPathSum(root, targetSum))
exit(0)