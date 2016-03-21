"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if numRows == 2:
            return s[0:len(s):2] + s[1:len(s):2]
        s = list(s)
        b = numRows * 2 - 2 - len(s) % (numRows * 2 - 2)
        for i in xrange(b):
            s.append(None)
        m = len(s) / (numRows * 2 - 2)
        list1 = []
        for i in xrange(m):
            list1.append(s[i * (numRows * 2 - 2):(i + 1) * (numRows * 2 - 2)])
        # print list1
        list2 = []
        for i in xrange(len(list1)):
            list2.append(list1[i][:numRows])
            mid = list1[i][numRows:][::-1]
            mid.append(None)
            mid.insert(0, None)
            list2.append(mid)
        # print list2
        list3 = []
        for i in xrange(numRows):
            for j in xrange(2 * m):
                if list2[j][i] is not None:
                    list3.append(list2[j][i])
        # print list3
        return ''.join(list3)
s = Solution()
print s.convert("PIASIHLGNPYRAI", 5)

