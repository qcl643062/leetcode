#coding=utf-8
"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.
"""

class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #统计节点深度
        def numofnode(root):
            if root == None:
                return 0
            def priorder(root):
                if not root:
                    return 0
                return 1 + max(priorder(root.left), priorder(root.right))
            return priorder(root)

        #判断一个节点是否符合
        def nodetrue(root):
            if not root:
                return True
            numofleft = numofnode(root.left)
            numofright = numofnode(root.right)
            if abs(numofright - numofleft) <= 1:
                return True
            else:
                return False

        #对每个节点进行判断
        result = nodetrue(root)
        if result == False:
            return False
        boo1 = True
        boo2 = True
        if root:
            if root.left:
                boo1 = self.isBalanced(root.left)
                if boo1 == False:
                    return False
            if root.right:
                boo2 = self.isBalanced(root.right)
                if boo2 == False:
                    return False
        return True
s = Solution()
print s.isBalanced(TreeNode(0, TreeNode(1, TreeNode(2))))
