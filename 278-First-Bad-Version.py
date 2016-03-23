"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product 
fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. 
you should minimize the number of calls to the API.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        global first
        first = 1
        def check(n):
            global first
            if n == 1:
                first = first
            elif n == 2:
                if isBadVersion(1):
                    first = first
                else:
                    first = 1 + first
            else:
                if isBadVersion(n / 2 + first):
                    n = n / 2 + 1
                    return check(n)
                else:
                    first = first + n / 2
                    return check(n / 2 + 1)
        check(n)
        return first