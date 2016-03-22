"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the 
sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                if i + 1 < m and j + 1 < n:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
                elif i + 1 >= m and j + 1 < n:
                    grid[i][j] += grid[i][j + 1]
                elif i + 1 < m and j + 1 >= n:
                    grid[i][j] += grid[i + 1][j]
                else:
                    pass
        return grid[0][0]
s = Solution()
print s.minPathSum([[1,2,3],[2,3,4]])