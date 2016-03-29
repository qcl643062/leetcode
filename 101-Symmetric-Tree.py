"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        a = []
        b = []
        e = []
        def left(root):
            if root.left != None:
                left(root.left)
            a.append(root.val)
            if root.right != None:
                left(root.right)
        left(root)
        if a[:len(a) / 2] == a[len(a) / 2 + 1:][::-1]:
            c = True
        else:
            return False
            
        def left1(root):
            if root.left != None:
                left1(root.left)
            if root.right != None:
                left1(root.right)
            b.append(root.val)
        left1(root)

        def right1(root):
            if root.right != None:
                right1(root.right)
            if root.left != None:
                right1(root.left)
            e.append(root.val)
        right1(root)
 
        if b == e:
            d = True
        else:
            return False
        return True
s = Solution()
print s.isSymmetric(TreeNode(0, TreeNode(1), TreeNode(1)))