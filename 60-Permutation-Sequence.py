#coding=utf-8
"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial
        a = [str(i + 1) for i in xrange(n)]
        b = []
        while k > 0:
            changer = k / factorial(n - 1)
            k = k % factorial(n - 1)
            if k == 0:
                b.append(a[changer - 1])
                del a[changer - 1]
                return ''.join(b) + ''.join(a)[::-1]
            else:
                b.append(a[changer])
                del a[changer]
                n = n - 1
s = Solution()
print s.getPermutation(10, 456)