"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:

A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        if nums[0] >= len(nums) - 1:
            return True
        m = len(nums) - 1
        for i in range(len(nums) - 1)[::-1]:
            if nums[i] >= m - i:
                m = i
            if i == 0:
                if nums[i] >= m:
                    return True
                else:
                    return False

s = Solution()
print s.canJump([3,2,1,0,4])

