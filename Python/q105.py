# 105. Construct Binary Tree from Preorder and Inorder Traversal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        val = preorder[0]
        root_index = inorder.index(val)
        inorder_left = inorder[0:root_index]
        inorder_right = inorder[root_index+1:]
        preorder_left = preorder[1:1+len(inorder_left)]
        preorder_right = preorder[1+len(inorder_left):]
        leftTree = self.buildTree(preorder_left, inorder_left)
        rightTree = self.buildTree(preorder_right, inorder_right)
        return TreeNode(val=val, left=leftTree, right=rightTree)


s = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
rootNode = s.buildTree(preorder, inorder)
exit(0)