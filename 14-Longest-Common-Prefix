"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def common(a, b):
            m = min(len(a), len(b))
            for i in xrange(m):
                if a[i] != b[i]:
                    if i == 0:
                        return ''
                    else:
                        return a[:i]
            else:
                return a[:m]
            
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        b = strs[0]
        for i in xrange(1, len(strs)):
            b = common(b, strs[i])
            if b == '':
                return ''
        return b
s = Solution()
print s.longestCommonPrefix(['aaa', 'aab'])