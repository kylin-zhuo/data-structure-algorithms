"""
57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

"""


# Definition for an interval.
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
        # itvs = sorted(intervals + [newInterval], key=lambda x: x.start)
        # res = []
        # for i in range(len(itvs) - 1):
        #     if itvs[i].end >= itvs[i+1].start:
        #         itvs[i].end = max(itvs[i].end, itvs[i+1].end)
        #     else:
        #         res.append(itvs[i])
        # return res
        s, e = newInterval.start, newInterval.end
        left, right, merge = [], [], []
        for it in intervals:
            if it.end < s: left.append(it)
            elif it.start > e: right.append(it)
            else: merge.append(it)
        print left, right, merge
        return left + ([Interval(min(s, merge[0].start), max(e, merge[-1].end))] if merge else [newInterval]) + right 
        