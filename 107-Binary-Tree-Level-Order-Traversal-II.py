#coding=utf-8
"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        a = [root]
        b = []
        c = []
        d = []
        while a != []:
            for i in range(len(a)):
                #可以用双向队列的leftpop来写
                last = a[0]
                del a[0]
                c.append(last.val)
                if last.left or last.right:
                    if last.left:
                        b.append(last.left)
                    if last.right:
                        b.append(last.right)
                else:
                    pass
            d.append(c)
            a = b[::]
            b = []
            c = []
        return d[::-1]
s = Solution()
print s.levelOrderBottom(TreeNode(0, TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))))