#coding=utf-8
"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) < 4:
            return []
        listofall = []
        if 4 * nums[-1] >= target:
            for i in range(len(nums)):
                if 4 * nums[i] <= target:
                    for j in range(i + 1, len(nums)):
                        if nums[i] + 3 * nums[j] <= target:
                            r = len(nums) - 1
                            l = j + 1
                            while l < r:
                                if nums[i] + nums[j] + nums[l] + nums[r] > target:
                                    r = r - 1
                                elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                                    l = l + 1
                                else:
                                    if [nums[i], nums[j], nums[l], nums[r]] not in listofall:
                                        listofall.append([nums[i], nums[j], nums[l], nums[r]])
                                    r = r - 1
                                    l = l + 1
        return listofall
s = Solution()
print s.fourSum([1,2,45,6,4,7], 12)