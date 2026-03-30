import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = {}
        for num in nums:
            counted[num] = counted.get(num, 0) + 1

        heap = []
        for num in counted.keys():
            heapq.heappush(heap, (counted[num], num))
            if len(heap) > k:
                heapq.heappop(heap)


        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result