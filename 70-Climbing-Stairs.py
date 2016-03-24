"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        list1 = [1, 2]
        for i in range(2, n):
            list1.append(list1[i - 1] + list1[i - 2])
        return list1[n - 1]
s = Solution()
print s.climbStairs(6)