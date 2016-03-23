"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        b = 0 
        y = x       
        while x / 10 > 0:
            b = b * 10 + x % 10
            x = x / 10
        b = b * 10 + x
        if b > 2147483647:
            return False
        if b != y:
            return False
        else:
            return True
s = Solution()
print s.isPalindrome(100)
