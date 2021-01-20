# 99. Recover Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.val = []
        self.tree_node = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.val.append(root.val)
            self.tree_node.append(root)
            inorder(root.right)

        inorder(root)
        self.val.sort()
        for i in range(0, len(self.tree_node)):
            self.tree_node[i].val = self.val[i]
