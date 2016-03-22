"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right 
corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = [1] * m
        b = [a] * n
        for i in range(1, len(b)):
            for j in range(1, len(b[0])):
                b[i][j] = b[i - 1][j] + b[i][j - 1]
        return b[n-1][m-1]
s = Solution()
print s.uniquePaths(5, 8)