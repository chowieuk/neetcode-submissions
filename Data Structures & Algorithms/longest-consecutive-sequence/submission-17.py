from collections import defaultdict
from typing import List

# Input: nums = [2,20,4,10,3,4,5]
# Set: {2,3,4,5,10,20}
# Sorted: [2, 3, 4, 4, 5, 10, 20]
# Output: 4


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums:
                current = num
                length = 1
            
                while current + 1 in nums:
                    current += 1
                    length += 1

                longest = max(longest, length)
        
        return longest        