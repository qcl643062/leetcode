"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda x:x.start, reverse = 1)
        def compare(x):
            if x[0].end < x[1].start:
                return x, 0
            else:
                return Interval(x[0].start, max(x[1].end, x[0].end)), 1
        list1 = [intervals[-1], intervals[-2]]
        list2 = []
        intervals.pop()
        intervals.pop()
        while intervals != []:
            a, b = compare(list1)
            if b == 0:
                list2.append(a[0])
                list1 = [a[-1]]
                list1.append(intervals.pop())
            else:
                list1 = []
                list1.append(a)
                list1.append(intervals.pop())
        a, b = compare(list1)
        if b == 0:
            list2 = list2 + a
        else:
            list2.append(a)
        return list2
s = Solution()
print s.merge([Interval(1, 3), Interval(2, 6)])