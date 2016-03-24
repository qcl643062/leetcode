#coding=utf-8
"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        global a
        a = ''
        # 处理一个字符的时候
        def one(s):
            global a
            if s == '1':
                a = a + 'I'
            if s == '2':
                a = a + 'II'
            if s == '3':
                a = a + 'III'
            if s == '4':
                a = a + 'IV'
            if s == '5':
                a = a + 'V'
            if s == '6':
                a = a + 'VI'
            if s == '7':
                a = a + 'VII'
            if s == '8':
                a = a + 'VIII'
            if s == '9':
                a = a + 'IX'
            
            return a
            # 处理2个字符
        def two(s):
            global a
            if s[0] == '1':
                a = a + 'X'
                return one(s[1])
            if s[0] == '2':
                a = a + 'XX'
                return one(s[1])
            if s[0] == '3':
                a = a + 'XXX'
                return one(s[1])
            if s[0] == '4':
                a = a + 'XL'
                return one(s[1])
            if s[0] == '5':
                a = a + 'L'
                return one(s[1])
            if s[0] == '6':
                a = a + 'LX'
                return one(s[1])
            if s[0] == '7':
                a = a + 'LXX'
                return one(s[1])
            if s[0] == '8':
                a = a + 'LXXX'
                return one(s[1])
            if s[0] == '9':
                a = a + 'XC'
                return one(s[1])
            if s[0] == '0':
                return one(s[1])
            # 处理3个字符
        def three(s):
            global a
            if s[0] == '1':
                a = a + 'C'
                return two(s[1:])
            if s[0] == '2':
                a = a + 'CC'
                return two(s[1:])
            if s[0] == '3':
                a = a + 'CCC'
                return two(s[1:])
            if s[0] == '4':
                a = a + 'CD'
                return two(s[1:])
            if s[0] == '5':
                a = a + 'D'
                return two(s[1:])
            if s[0] == '6':
                a = a + 'DC'
                return two(s[1:])
            if s[0] == '7':
                a = a + 'DCC'
                return two(s[1:])
            if s[0] == '8':
                a = a + 'DCCC'
                return two(s[1:])
            if s[0] == '9':
                a = a + 'CM'
                return two(s[1:])
            if s[0] == '0':
                return two(s[1:])
            # 最后处理4个字符的情况
        def four(s):
            global a
            if s[0] == '1':
                a = a + 'M'
                return three(s[1:])
            if s[0] == '2':
                a = a + 'MM'
                return three(s[1:])
            if s[0] == '3':
                a = a + 'MMM'
                return three(s[1:])
            if s[0] == '0':
                return three(s[1:])
        num = str(num)
        if len(num) == 1:
            return one(num)
        if len(num) == 2:
            return two(num)
        if len(num) == 3:
            return three(num)
        if len(num) ==4:
            return four(num)
s = Solution()
print s.intToRoman(1234)