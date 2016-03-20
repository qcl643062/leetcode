"""
Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which 
the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        m = []
        maxofamount = 0
        for i in xrange(len(s)):
            middle = ''
            count = 0
            for j in xrange(i, len(s)):
                if s[j] not in middle:
                    middle += s[j]
                    count += 1
                    if j == len(s) - 1:
                        if count > maxofamount:
                            return count
                        else:
                            return maxofamount
                    if count >= 95:
                        return 95
                else:
                    if count > maxofamount:
                        maxofamount = count
                    break
        return maxofamount
s = Solution()
print s.lengthOfLongestSubstring("cdd")
