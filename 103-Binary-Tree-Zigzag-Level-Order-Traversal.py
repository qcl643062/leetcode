"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if  not root:
            return []
        a = []
        queue = [root]
        b = 0
        while queue:
            if b == 0:
                a.append([q.val for q in queue])
            else:
                a.append([q.val for q in queue][::-1])
            queue = [q for node in queue for q in (node.left, node.right) if q]
            if b == 0:
                b = 1
            else:
                b = 0
        return a

s = Solution()
print s.zigzagLevelOrder(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(3)))
