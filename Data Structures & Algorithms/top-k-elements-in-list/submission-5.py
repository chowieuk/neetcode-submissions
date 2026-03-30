class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can use bucket sort here because the maximum frequency 
        # is bound by the length of the array

        # create frequency map
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        
        print(freqs)
        buckets = [[] for _ in range(len(nums) + 1)]
        print(buckets)
        for val, count in freqs.items():
            print(val,count)
            buckets[count].append(val)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result