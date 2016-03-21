"""
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list1 = []
        if nums1:
            if nums2:
                m = n = 0
                while m < len(nums1) and n < len(nums2):
                    if nums1[m] < nums2[n]:
                        list1.append(nums1[m])
                        m += 1
                    else:
                        list1.append(nums2[n])
                        n += 1
                if m == len(nums1):
                    list1.extend(nums2[n:])
                else:
                    list1.extend(nums1[m:])
            else:
                list1 = nums1
        else:
            if nums2:
                list1 = nums2
            else:
                return None
        if len(list1) % 2 == 0:
            return (list1[len(list1) / 2] + list1[len(list1) / 2 - 1]) / 2.0
        else:
            return float(list1[len(list1) / 2])

# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         nums1.extend(nums2)
#         nums1.sort()
#         if len(nums1) % 2 == 0:
#             return (nums1[len(nums1) / 2] + nums1[len(nums1) / 2 - 1]) / 2.0
#         else:
#             return nums1[len(nums1) / 2]
s = Solution()
print s.findMedianSortedArrays([1, 2], [1, 2])
