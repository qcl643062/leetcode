"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = '*'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '*':
                    for k in range(n):
                        if matrix[i][k] != '*':
                            matrix[i][k] = 0
                    for h in range(m):
                        if matrix[h][j] != '*':
                            matrix[h][j] = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '*':
                    matrix[i][j] = 0
                    