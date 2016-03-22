"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phonenumber = [[' '], ['*'],['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h','i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q','r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return phonenumber[int(digits)]
        else:
            result = phonenumber[int(digits[0])]
            for i in range(1, len(digits)):
                m = []
                for j in result:
                    for k in phonenumber[int(digits[i])]:
                        m.append(j + k)
                result = m
        return result
s = Solution()
print s.letterCombinations('23')