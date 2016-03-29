"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        a = [root]
        num = 1
        b = []
        while True:
            for i in a:
                if i.left or i.right:
                    if i.left:
                        b.append(i.left)
                    if i.right:
                        b.append(i.right)
                else:
                    return num
            else:
                num = num + 1
                a = b[::]
                b = []
s = Solution()
print s.minDepth(TreeNode(0, TreeNode(1, TreeNode(2, TreeNode(3)))))

