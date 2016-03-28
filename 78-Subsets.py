"""
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a = [[]]
        if nums == []:
            return a
        nums = sorted(list(set(nums)))
        for i in nums:
            for j in xrange(len(a)):
                x = a[j][::]
                a[j].append(i)
                a = a + [x]
        return a
s = Solution()
print s.subsets([1, 2, 3])

