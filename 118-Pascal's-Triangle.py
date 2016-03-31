"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        listofall = [[1], [1, 1]]
        listoffirst = [1, 1]
        listofmiddle = [1]
        while numRows - 2 > 0:
            for i in range(len(listoffirst) - 1):
                listofmiddle.append(listoffirst[i] + listoffirst[i + 1])
            listofmiddle.append(1)
            listofall.append(listofmiddle)
            listoffirst = listofmiddle
            listofmiddle = [1]
            numRows = numRows - 1
        return listofall

s = Solution()
print s.generate(10)