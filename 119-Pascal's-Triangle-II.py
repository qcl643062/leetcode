"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        List = [0] * (rowIndex + 1)
        for i in range(rowIndex+1):
            if i == 0:
                List[i] = [1]
            elif i== 1:
                List[i] = [1,1]
            else:
                List[i] = [0]*(i+1)
                List[i][0] = List[i][i] = 1
                for j in range(1,i):
                    List[i][j] = List[i-1][j-1]+List[i-1][j]
        return List[rowIndex]

s = Solution()
print s.getRow(4)