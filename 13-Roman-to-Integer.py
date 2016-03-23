"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        global a
        a = 0
        def xlevel(s):
            global a
            if s.count('X') == 1:
                a = a + 9
            elif s.count('V'):
                if len(s) ==1:
                    a = a + 5
                if len(s) == 2:
                    if s[0] == 'V':
                        a = a + 6
                    else:
                        a = a + 4
                if len(s) == 3:
                    a = a + 7
                if len(s) == 4:
                    a = a + 8
            else:
                a = a + s.count('I')
            return a
        def llevel(s):
            global a
            if s.count('L'):
                if s[0] != "L":
                    a = a + 40
                    return xlevel(s[2:])
                else:
                    for i in range(1,len(s)):
                        if s[i] != 'X':
                            a = a + 50 + (i - 1) * 10
                            return xlevel(s[i:])
                    else:
                        a = a + 50 + (len(s) - 1) * 10
                        return a
            else:
                for i in range(len(s)):
                    if s[i] != 'X':
                        a = a + i * 10
                        return xlevel(s[i:])
                else:
                    a = a + len(s) * 10
                    return a
        def dlevel(s):
            global a
            if s.count('D'):
                if s[0] != "D":
                    a = a + 400
                    if s[2:].count('C'):
                        a = a + 90
                        return xlevel(s[4:])
                    else:
                        return llevel(s[2:])
                else:
                    for i in range(1, len(s)):
                        if s[i] != 'C':
                            a = a + 500 + (i - 1) * 100
                            # print a
                            if s[i:].count('C') == 1:
                                a = a + 90
                                return xlevel(s[i + 2:])
                            else:
                                return llevel(s[i:])
                    else:
                        a = a + 500 + (len(s) - 1) * 100
                        return a
            else:
                if s.count('C') == 4:
                    a = a + 390
                    return xlevel(s[5:])
                if s.count('C') == 3:
                    if s[2] == 'C':
                        a = a + 300
                        return llevel(s[3:])
                    else:
                        a = a + 290
                        return xlevel(s[4:])
                if s.count('C') == 2:
                    if s[1] == 'C':
                        a = a + 200
                        return llevel(s[2:])
                    else:
                        a = a + 190
                        return xlevel(s[3:])
                if s.count('C') == 1:
                    if s[0] == 'C':
                        a = a + 100
                        return llevel(s[1:])
                    else:
                        a = a + 90
                        return xlevel(s[2:])
                if s.count('C') == 0:
                    return llevel(s)
        if s.count("M") == 4:
            a = a + 3900
            if s[5:].count('C') == 1:
                a = a + 90
                # print s[7:]
                return xlevel(s[7:])
            else:
                return llevel(s[5:])
        if s.count('M') == 3:
            if s[2] == 'M':
                a = a + 3000
                return dlevel(s[3:])
            else:
                a = a + 2900
                if s[4:].count('C') == 1:
                    a = a + 90
                # print s[7:]
                    return xlevel(s[6:])
                else:
                    return llevel(s[4:])
        if s.count('M') == 2:
            if s[1] == 'M':
                a = a + 2000
                return dlevel(s[2:])
            else:
                a = a + 1900
                if s[3:].count("C") == 1:
                    a = a + 90
                    return xlevel(s[5:])
                else:
                    return llevel(s[3:])
        if s.count('M') == 1:
            if s[0] =='M':
                a = a + 1000
                return dlevel(s[1:])
            else:
                a = a + 900
                if s[2:].count('C') == 1:
                    a = a + 90
                    return xlevel(s[4:])
                else:
                    return llevel(s[2:])
        if s.count('M') == 0:
            return dlevel(s)
s = Solution()
print s.romanToInt('MCM')