from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        count = 0
        while l < r:
            if height[l] <= height[l+1]:
                l += 1
                continue
            elif height[r - 1] >= height[r]:
                r -= 1
                continue
            if height[l] < height[r]:
                foo = height[l]
                while l < r and height[l + 1] < foo:
                    count += foo - height[l + 1]
                    l += 1
            else:
                bar = height[r]
                while l < r and height[r - 1] < bar:
                    count += bar - height[r - 1]
                    r -= 1
                
        return count
            