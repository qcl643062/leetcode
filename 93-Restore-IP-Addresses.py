"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        b = []
        def check(s):
            for i in range(len(s) -1, -1, -1):
                a = s[i].split('.')
                for j in range(len(a)):
                    if int(a[j]) > 255:
                        s.remove(s[i])
                        break
                    if len(a[j]) > 1:
                        if a[j][0] == '0':
                            s.remove(s[i])
                            break
            return s
        if len(s) < 4 or len(s) > 12:
            return []
        if len(s) == 4:
            b.append(s[0] + '.' + s[1] + '.' + s[2] + '.' + s[3])
            return check(b)
        if len(s) == 5:
            b.append(s[:2] + '.' + s[2] + '.' + s[3] + '.' + s[4])
            b.append(s[0] + '.' + s[1:3] + '.' + s[3] + '.' + s[4])
            b.append(s[0] + '.' + s[1] + '.' + s[2:4] + '.' + s[4])
            b.append(s[0] + '.' + s[1] + '.' + s[2] + '.' + s[3:])
            return check(b)
        if len(s) == 6:
            b.append(s[:2] + '.' + s[2:4] + '.' + s[4] + '.' + s[5])
            b.append(s[:2] + '.' + s[2] + '.' + s[3:5] + '.' + s[5])
            b.append(s[:2] + '.' + s[2] + '.' + s[3] + '.' + s[4:])
            b.append(s[0] + '.' + s[1:3] + '.' + s[3:5] + '.' + s[5])
            b.append(s[0] + '.' + s[1:3] + '.' + s[3] + '.' + s[4:])
            b.append(s[0] + '.' + s[1] + '.' + s[2:4] + '.' + s[4:])
            b.append(s[:3] + '.' + s[3] + '.' + s[4] + '.' + s[5])
            b.append(s[0] + '.' + s[1:4] + '.' + s[4] + '.' + s[5])
            b.append(s[0] + '.' + s[1] + '.' + s[2:5] + '.' + s[5])
            b.append(s[0] + '.' + s[1] + '.' + s[2] + '.' + s[3:])
            return check(b)
        if len(s) == 7:
            b.append(s[0:2] + '.' + s[2:5] + '.' + s[5] + '.' + s[6])
            b.append(s[0:2] + '.' + s[2] + '.' + s[3:6] + '.' + s[6])
            b.append(s[0:2] + '.' + s[2] + '.' + s[3] + '.' + s[4:])
            b.append(s[0] + '.' + s[1:3] + '.' + s[3:5] + '.' + s[5:])
            b.append(s[0] + '.' + s[1:3] + '.' + s[3] + '.' + s[4:])
            b.append(s[0] + '.' + s[1] + '.' + s[2:4] + '.' + s[4:])
            b.append(s[0:3] + '.' + s[3:5] + '.' + s[5] + '.' + s[6])
            b.append(s[0:3] + '.' + s[3] + '.' + s[4:6] + '.' + s[6])
            b.append(s[0:3] + '.' + s[3] + '.' + s[4] + '.' + s[5:])
            b.append(s[0] + '.' + s[1:4] + '.' + s[4:6] + '.' + s[6])
            b.append(s[0] + '.' + s[1:4] + '.' + s[4] + '.' + s[5:])
            b.append(s[0] + '.' + s[1] + '.' + s[2:5] + '.' + s[5:])
            b.append(s[0:2] + '.' + s[2:4] + '.' + s[4:6] + '.' + s[6])
            b.append(s[0:2] + '.' + s[2:4] + '.' + s[4] + '.' + s[5:])
            b.append(s[0:2] + '.' + s[2] + '.' + s[3:5] + '.' + s[5:])
            b.append(s[0] + '.' + s[1:3] + '.' + s[3:6] + '.' + s[6])
            return check(b)
        if len(s) == 8:
            b.append(s[0:3] + '.' + s[3:6] + '.' + s[6] + '.' + s[7])
            b.append(s[0:3] + '.' + s[3] + '.' + s[4:7] + '.' + s[7])
            b.append(s[0:3] + '.' + s[3] + '.' + s[4] + '.' + s[5:])
            b.append(s[0] + '.' + s[1:4] + '.' + s[4:7] + '.' + s[7])
            b.append(s[0] + '.' + s[1:4] + '.' + s[4] + '.' + s[5:])
            b.append(s[0] + '.' + s[1] + '.' + s[2:5] + '.' + s[5:])
            b.append(s[0:2] + '.' + s[2:4] + '.' + s[4:7] + '.' + s[7])
            b.append(s[0:2] + '.' + s[2:4] + '.' + s[4] + '.' + s[5:])
            b.append(s[0:2] + '.' + s[2] + '.' + s[3:5] + '.' + s[5:])
            b.append(s[0] + '.' + s[1:3] + '.' + s[3:5] + '.' + s[5:])
            b.append(s[0:2] + '.' + s[2:5] + '.' + s[5:7] + '.' + s[7])
            b.append(s[0:2] + '.' + s[2:5] + '.' + s[5] + '.' + s[6:])
            b.append(s[0:2] + '.' + s[2] + '.' + s[3:6] + '.' + s[6:])
            b.append(s[0] + '.' + s[1:3] + '.' + s[3:6] + '.' + s[6:])
            b.append(s[0:3] + '.' + s[3:5] + '.' + s[5:7] + '.' + s[7])
            b.append(s[0:3] + '.' + s[3:5] + '.' + s[5] + '.' + s[6:])
            b.append(s[0:3] + '.' + s[3] + '.' + s[4:6] + '.' + s[6:])
            b.append(s[0] + '.' + s[1:4] + '.' + s[4:6] + '.' + s[6:])
            b.append(s[0:2] + '.' + s[2:4] + '.' + s[4:6] + '.' + s[6:])
            return check(b)
        if len(s) == 9:
            b.append(s[0:2] + '.' + s[2:5] + '.' + s[5:8] + '.' + s[8])
            b.append(s[0:2] + '.' + s[2:5] + '.' + s[5] + '.' + s[6:])
            b.append(s[0:2] + '.' + s[2] + '.' + s[3:6] + '.' + s[6:])
            b.append(s[0] + '.' + s[1:3] + '.' + s[3:6] + '.' + s[6:])
            b.append(s[0:3] + '.' + s[3:5] + '.' + s[5:8] + '.' + s[8])
            b.append(s[0:3] + '.' + s[3:5] + '.' + s[5] + '.' + s[6:])
            b.append(s[0:3] + '.' + s[3] + '.' + s[4:6] + '.' + s[6:])
            b.append(s[0] + '.' + s[1:4] + '.' + s[4:6] + '.' + s[6:])
            b.append(s[0:3] + '.' + s[3:6] + '.' + s[6:8] + '.' + s[8])
            b.append(s[0:3] + '.' + s[3:6] + '.' + s[6] + '.' + s[7:])
            b.append(s[0:3] + '.' + s[3] + '.' + s[4:7] + '.' + s[7:])
            b.append(s[0] + '.' + s[1:4] + '.' + s[4:7] + '.' + s[7:])
            b.append(s[0:2] + '.' + s[2:4] + '.' + s[4:6] + '.' + s[6:])
            b.append(s[0:2] + '.' + s[2:4] + '.' + s[4:7] + '.' + s[7:])
            b.append(s[0:2] + '.' + s[2:5] + '.' + s[5:7] + '.' + s[7:])
            b.append(s[0:3] + '.' + s[3:5] + '.' + s[5:7] + '.' + s[7:])
            return check(b)
        if len(s) == 10:
            b.append(s[0:3] + '.' + s[3:6] + '.' + s[6:9] + '.' + s[9])
            b.append(s[0:3] + '.' + s[3:6] + '.' + s[6] + '.' + s[7:])
            b.append(s[0:3] + '.' + s[3] + '.' + s[4:7] + '.' + s[7:])
            b.append(s[0] + '.' + s[1:4] + '.' + s[4:7] + '.' + s[7:])
            b.append(s[0:3] + '.' + s[3:6] + '.' + s[6:8] + '.' + s[8:])
            b.append(s[0:3] + '.' + s[3:5] + '.' + s[5:8] + '.' + s[8:])
            b.append(s[0:3] + '.' + s[3:5] + '.' + s[5:7] + '.' + s[7:])
            b.append(s[0:2] + '.' + s[2:5] + '.' + s[5:8] + '.' + s[8:])
            b.append(s[0:2] + '.' + s[2:5] + '.' + s[5:7] + '.' + s[7:])
            b.append(s[0:2] + '.' + s[2:4] + '.' + s[4:7] + '.' + s[7:])
            return check(b)
        if len(s) == 11:
            b.append(s[0:3] + '.' + s[3:6] + '.' + s[6:9] + '.' + s[9:])
            b.append(s[0:3] + '.' + s[3:6] + '.' + s[6:8] + '.' + s[8:])
            b.append(s[0:3] + '.' + s[3:5] + '.' + s[5:8] + '.' + s[8:])
            b.append(s[0:2] + '.' + s[2:5] + '.' + s[5:8] + '.' + s[8:])
            return check(b)
        if len(s) == 12:
            b.append(s[0:3] + '.' + s[3:6] + '.' + s[6:9] + '.' + s[9:])
            return check(b)
s = Solution()
print s.restoreIpAddresses("25525511135")