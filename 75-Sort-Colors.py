#coding=utf-8
"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        if len(nums) == 2:
            if nums[0] == 0:
                return 
            elif nums[-1] == 2:
                return
            else:
                a = nums.pop()
                nums.insert(0, a)
        LocationOfRed = -1
        LocationOfWhite = -1
        #此处多加了一个blue
        nums.append(2)
        for i in range(len(nums) - 1):
            if nums[0] == 0:
                nums.insert(LocationOfRed, 0)
                del nums[0]
            elif nums[0] == 1:
                nums.insert(LocationOfWhite, 1)
                del nums[0]
                LocationOfRed = LocationOfRed - 1
            else:
                nums.append(2)
                del nums[0]
                LocationOfRed = LocationOfRed - 1
                LocationOfWhite = LocationOfWhite - 1
        nums.pop()
s = Solution()
m = [1,2,0,1,2]
s.sortColors(m)
print m