from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = {}
        result = []
        for num in nums:
            counted[num] = counted.get(num, 0) + 1
        result = sorted(counted, key=lambda num: counted[num], reverse=True)

        return result[:k]