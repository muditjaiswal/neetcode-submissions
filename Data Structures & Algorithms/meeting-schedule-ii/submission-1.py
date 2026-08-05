"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        i = 0
        j = 0
        curr_max = 0
        counter = 0
        while i < len(intervals) and j < len(intervals):
            if start[i] < end[j]:
                counter += 1
                i += 1
            elif end[j] < start[i]:
                counter -= 1
                j += 1
            else:
                j += 1
                i += 1
            curr_max = max(curr_max, counter)
        return curr_max
