"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

import re
from collections import Counter
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        m = Counter(s)
        if m['('] != m[')'] or m['{'] != m['}'] or m['['] != m[']']:
            return False
        for i in range(len(s) / 2):
            s = re.sub('\[\]|\(\)|\{\}', '', s)
            if s == '':
                return True
        else:
            return False
s = Solution()
print s.isValid('()()()(){})')