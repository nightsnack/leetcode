from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.route = []
        def preOrder( root: TreeNode, sum: int, path: List):
            if not root:
                return
            sum = sum + root.val
            path.append(root.val)
            if not root.left and not root.right and sum == targetSum:
                self.route.append(path)
            preOrder(root.left, sum, path.copy())
            preOrder(root.right, sum, path.copy())
        preOrder(root, 0, [])
        return self.route
root = TreeNode(5, left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))), right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, left=TreeNode(5), right=TreeNode(1))))
targetSum = 22
s = Solution()
print(s.pathSum(root, targetSum))
exit(0)