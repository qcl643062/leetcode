"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                nums = nums[i:]
                break
        else:
            return 1
        if nums[0] != 1:
            return 1
        else:
            for i in range(len(nums) - 1):
                if nums[i + 1] - nums[i] > 1:
                    return (nums[i] + 1)
            else:
                return (nums[-1] + 1)
s = Solution()
print s.firstMissingPositive([1,2,-1, 45])