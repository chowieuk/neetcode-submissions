from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []
        for i, v in enumerate(nums):
            heapq.heappush(max_heap, (-v, i))
            if i >= k - 1:
                while max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)
                res.append(-max_heap[0][0])
        return res