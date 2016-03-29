"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""


class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None:
            if q == None:
                return True
            else:
                return False
        else:
            if q == None:
                return False
        leftsum = rightsum = True
        if p.val != q.val:
            return False
        else:
            if p.left != None:
                if q.left != None:
                    if p.left.val != q.left.val:
                        return False
                    else:                        
                        leftsum = self.isSameTree(p.left, q.left)
                else:                  
                    return False
            else:
                if q.left != None:
                    return False
            if p.right != None:
                if q.right != None:
                    if p.right.val != q.right.val:
                        return False
                    else:
                        rightsum = self.isSameTree(p.right, q.right)

                else:
                    return False
            else:
                if q.right != None:
                    return False
        return leftsum & rightsum
s = Solution()
print s.isSameTree(TreeNode(0), TreeNode(1))