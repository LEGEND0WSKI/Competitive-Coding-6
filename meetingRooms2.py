
# // Time Complexity : O(nlog(n)) for sorting and minheap
# // Space Complexity :O(k) for heap 
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda  x:x[0])         # sort wrt col 0
        
        pq = []                                                     # min heap
        heapq.heappush(pq, intervals[0][1])

        for i in range(1,len(intervals)):
                if intervals[i][0] >= pq[0]:                        # if current min is more than heap item
                    heapq.heappop(pq)                               # pop minheap item
                heapq.heappush(pq,intervals[i][1])                  # push current max to heap 
        return len(pq)