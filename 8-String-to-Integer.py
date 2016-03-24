"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not 
see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). 
You are responsible to gather all the input requirements up front.
"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == '':
            return 0
        if str[0] != '+':
            if str[0] != '-':
                if ord(str[0]) >57:
                    return 0
                elif ord(str[0]) < 48:
                    return 0
                else:
                    pass
        if len(str) == 1:
            if str == "+":
                return 0
            elif str == '-':
                return 0
            else:
                return int(str)
        def math(s):
            a = ''
            for i in range(len(s)):
                if ord(s[i]) > 57:
                    break
                elif ord(s[i]) < 48:
                    break
                else:
                    a = a + s[i]
            if a != '':
                return int(a)
            else:
                return 0
                
            
        if str[0] == '+':
            if math(str[1:]) > 2147483647:
                return 2147483647
            else:
                return math(str[1:])
        elif str[0] == '-':
            if -math(str[1:]) < -2147483648:
                return -2147483648
            else:
                return (-math(str[1:]))
        else:
            
            if math(str) > 2147483647:
                return 2147483647
            else:
                return math(str)
s = Solution()
print s.myAtoi('+123')