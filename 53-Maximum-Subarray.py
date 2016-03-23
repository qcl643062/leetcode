#coding=utf-8
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        sumofall = nums[0]
        sumofpart = nums[0]
        for i in range(1, len(nums)):
            sumofall = max(sumofall, sumofpart + nums[i], nums[i])
            if sumofall == nums[i]:
                sumofpart = nums[i]
            else:
                sumofpart += nums[i]
            if sumofpart < 0:
                sumofpart = 0
        return sumofall
s = Solution()
print s.maxSubArray([1, -1, 2, -3, 3])