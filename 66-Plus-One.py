"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return 1
        digits = [str(digits[i]) for i in xrange(len(digits))]
        digit = int(''.join(digits))
        list1 = list(str(digit + 1))
        return [int(list1[i]) for i in xrange(len(list1))]
s = Solution()
print s.plusOne([1,2,3])