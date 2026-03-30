class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # number of buckets = len(nums) + 1
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        freqs = [[] for _ in range(len(nums) + 1)]

        for val, count in counts.items():
            freqs[count].append(val)

        result = []
        for i in range(len(freqs)-1,0,-1):
            for num in freqs[i]:
                result.append(num)
                if len(result) == k:
                    return result
