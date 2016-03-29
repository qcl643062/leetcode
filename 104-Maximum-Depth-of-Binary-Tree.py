"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:        
            return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

s = Solution()
print s.maxDepth(TreeNode(0, TreeNode(1), TreeNode(2, TreeNode(2))))