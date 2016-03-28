"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals == []:
            return [newInterval]
        list1 = []
        for i in intervals:
            list1.append(i.start)
            list1.append(i.end)
        list1.append(newInterval.start)
        list1.append(newInterval.end)
        list1.sort()
        a = list1.index(newInterval.start)
        b = list1.index(newInterval.end)
        if a % 2 == 0:
            if b % 2 == 0:                
                list1 = list1[:a + 1] + list1[b+ 1:]
            else:
                if b != len(list1) - 1:
                    if list1[b] != list1[b + 1]:
                        list1 = list1[:a + 1] + list1[b:]
                    else:
                        list1 = list1[:a + 1] + list1[b + 2:]
                else:
                    list1 = list1[:a + 1] + list1[b:]
        else:
            if b % 2 == 0:
                list1 = list1[:a] + list1[b + 1:]
            else:
                if b != len(list1) - 1:
                    if list1[b] != list1[b + 1]:
                        list1 = list1[:a] + list1[b:]
                    else:
                        list1 = list1[:a] + list1[b + 2:]
                else:
                    list1 = list1[:a] + list1[b:]
        list2 = []
        for i in range(0, len(list1), 2):
            list2.append(Interval(list1[i], list1[i + 1]))
        return list2
s = Solution()
m = s.insert([Interval(1, 2), Interval(3, 5)], Interval(2, 4))
for i in m:
    print i.start, i.end