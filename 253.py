"""
253 Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        heap = TheHeap()
        intervals = sorted(intervals, key=lambda x: x.start)
        heap.push(intervals[0])
        for i in range(1, len(intervals)):
            curr = intervals[i]
            prev = heap.pop()
            if curr.start >= prev.end: 
                prev.end = curr.end    
            else:
                heap.push(curr)
            heap.push(prev)
        return heap.get_length()
    

class TheHeap(object):
    def __init__(self, initial=None, key=lambda x:x.end):
        self.key = key
        if initial:
            self._data = [(key(item), item) for item in initial]
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self._data)[1]
    
    def get_length(self):
        return len(self._data)
