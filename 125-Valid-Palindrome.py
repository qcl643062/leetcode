"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        import re
        """
        :type s: str
        :rtype: bool
        """
        
        
        s = s.lower()
        m = re.findall('\w+', s)
        a = ''.join(m)
       
        for i in range(len(a) / 2 ):
            if a[i] != a[len(a) - i - 1]:
                return False
        else:
            return True

s = Solution()
print s.isPalindrome('ASl,,asdf')