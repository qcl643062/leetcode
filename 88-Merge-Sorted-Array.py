"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(len(nums1))[::-1]:
                del nums1[i]
            for i in range(len(nums2)):
                nums1.append(nums2[i])
        else:
            if n != 0:
                for i in range(m, len(nums1))[::-1]:
                    del nums1[i]
                i = 0
                j = 0
                while True:
                    if nums1[i] <= nums2[j]:
                        if i != len(nums1) - 1:
                            i = i + 1
                        else:
                            for k in range(j, len(nums2)):
                                nums1.append(nums2[k])
                            break
                    else:
                        nums1.insert(i, nums2[j])
                        if j == len(nums2) - 1:
                            break
                        j = j + 1
                        i = i + 1