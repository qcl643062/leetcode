"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.

"""

class Solution(object):
    def location(self, l, nums):
        if nums[l] >= len(nums) - 1 - l:
            return len(nums) - 1
        if nums[l] == 1:
            return l + 1
        list1 = []
        for i in xrange(1, nums[l] + 1):
            list1.append(i + nums[l + i])
        index1 = list1.index(max(list1))
        return index1 + 1 + l
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            return 1
        length = 0
        number = 0
        while length != len(nums) - 1:
            number += 1
            length = self.location(length, nums)
        return number
s = Solution()
print s.jump([2,0,2,0,1])
