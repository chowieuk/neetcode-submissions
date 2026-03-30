"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for meeting in intervals:
            if len(min_heap) > 0 and min_heap[0] <= meeting.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, meeting.end)

        return len(min_heap)