"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list1 = []
        list2 = sorted(nums)
    
        for i in range(len(nums)):
            if target - list2[i] in nums:
                if list2[i] * 2 == target:
                    a = nums.index(list2[i])
                    list1.append(a)
                    list1.append(nums[a + 1:].index(list2[i]) + a + 1)
                else:
                    list1.append(nums.index(list2[i]))
                    list1.append(nums.index(target - list2[i]))
                    list1.sort()
                return list1
s = Solution()
print s.twoSum([2, 7, 11, 15], 9)