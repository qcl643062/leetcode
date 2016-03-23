"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        global start
        start = 0
        global end
        end = 0
        result = []
        def erfen(nums):
            global start
            global end
            if nums == []:
                start = -1
                end = -1
            elif len(nums) == 1:
                if nums[0] == target:
                    start = start
                    end = end
                else:
                    start = -1
                    end = -1
            else:
                if nums[len(nums) / 2] == target:
                    for i in range(len(nums) / 2):
                        if nums[len(nums) / 2 - 1 - i] != target:
                            start = len(nums) / 2 - i + start
                            break
                    else:
                        start = start
                    if len(nums) / 2 + 1  == len(nums):
                        end = end + len(nums) / 2
                    else:
                        if len(nums) % 2 == 0:
                            for j in range(1, len(nums) / 2):
                                if nums[len(nums) / 2 + j] != target:
                                    end = len(nums) / 2 + j + end -1
                                    break
                            else:
                                end = len(nums) - 1 + end
                        else:
                            for j in range(1, len(nums) / 2 + 1):
                                if nums[len(nums) / 2 + j] != target:
                                    end = len(nums) / 2 + j + end - 1
                                    break
                            else:
                                end = len(nums) - 1 + end
                elif nums[len(nums) / 2] < target:
                    start = len(nums) / 2 + start
                    end = len(nums) / 2 + end
                    return erfen(nums[len(nums) / 2:])
                else:
                    return erfen(nums[:len(nums) / 2])
        erfen(nums)
        result.append(start)
        result.append(end)
        return result
s = Solution()
print s.searchRange([1, 2, 3, 3, 4], 3)