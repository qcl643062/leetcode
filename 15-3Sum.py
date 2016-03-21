#coding=utf-8
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        alloflist = []
        nums.sort()
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        for i in range(len(nums)):
            if nums[i] <= 0:
                if i == 0:
                    j = i + 1
                    k = len(nums) - 1
                    while j < k:
                        if nums[j] + nums[k] < -nums[i]:
                            j = j + 1
                        elif nums[j] + nums[k] > -nums[i]:
                            k = k - 1
                        else:
                            if [nums[i], nums[j], nums[k]] not in alloflist:
                                alloflist.append([nums[i], nums[j], nums[k]])
                            j = j + 1
                            k = k - 1
                else:
                    if nums[i] == nums[i - 1]:
                        pass
                    else:
                        j = i + 1
                        k = len(nums) - 1
                        while j < k:
                            if nums[j] + nums[k] < -nums[i]:
                                j = j + 1
                            elif nums[j] + nums[k] > -nums[i]:
                                k = k - 1
                            else:
                                if [nums[i], nums[j], nums[k]] not in alloflist:
                                    alloflist.append([nums[i], nums[j], nums[k]])
                                j = j + 1
                                k = k - 1
            else:
                break
        return alloflist
s = Solution()
print s.threeSum([-2, -1, 3, 0])