# 98. Validate Binary Search Tree
# create tree cannot make it as same as question. So there is a bug of running this code
import math
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = [(root, -math.inf, math.inf)]
        while stack:
            root_node, lower, upper  = stack.pop()
            if not root_node:
                continue
            val = root_node.val
            if val <= lower or val >= upper:
                return False
            stack.append((root_node.right, val, upper))
            stack.append((root_node.left, lower, val))
        return True




    def create_tree(self, nodelist: List) -> TreeNode:
        root = TreeNode(nodelist.pop(0))
        stack = [root]
        while nodelist:
            root_node = stack.pop(0)
            # if (len(nodelist)==0):
            #     root_node = None
            #     continue
            root_node.left = TreeNode(nodelist.pop(0))
            root_node.right = TreeNode(nodelist.pop(0))
            stack.append(root_node.left)
            stack.append(root_node.right)
        return root

s = Solution()
treenode = s.create_tree(nodelist = [5,1,7,None,None,3,9])
print(s.isValidBST(treenode))
exit(0)