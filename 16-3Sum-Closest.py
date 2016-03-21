"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def threeSum(nums, sum1):
            nums=sorted(nums)
            n=len(nums)
            if n==0:
                return 0
            if n <= 3:
                if sum(nums) == sum1:
                    return True
                else:
                    return None
            i=0
            while i<n:
                l,r=i+1,n-1
                target=sum1 -nums[i]
                while l<r:
                    if nums[l]+nums[r]==target:
                        return sum1
                    elif nums[l]+nums[r] < target:
                        l+=1
                    else:
                        r-=1
                i = i + 1
            else:
                return None
        for i in range(10000):
            if i == 0 and threeSum(nums, target) != None:
                return target
            else:
                if threeSum(nums, target + i) != None:
                    return target + i
                if threeSum(nums, target - i) != None:
                    return target - i
s = Solution()
print s.threeSumClosest([1,3,5,8,4], 11)