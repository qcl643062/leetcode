"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.list1 = []
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        a = b = True
        if root.left:
            a = self.isValidBST(root.left)
            if a == False:
                return False
        self.list1.append(root.val)
        if len(self.list1) > 1:
            if self.list1[-1] <= self.list1[-2]:
                return False
        if root.right:
            b = self.isValidBST(root.right)
            if b == False:
                return False
        return a and b

s = Solution()
print s.isValidBST(TreeNode(0))


