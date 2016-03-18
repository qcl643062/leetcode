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

