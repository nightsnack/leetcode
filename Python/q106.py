# 106. Construct Binary Tree from Inorder and Postorder Traversal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        val = postorder[-1]
        root_index = inorder.index(val)
        inorder_left = inorder[0:root_index]
        inorder_right = inorder[root_index+1:]
        postorder_left = postorder[0:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):-1]
        leftTree = self.buildTree(inorder_left, postorder_left)
        rightTree = self.buildTree(inorder_right, postorder_right)
        return TreeNode(val=val, left=leftTree, right=rightTree)


s = Solution()
postorder = [9,15,7,20,3]
inorder = [9,3,15,20,7]
rootNode = s.buildTree(inorder, postorder)
exit(0)