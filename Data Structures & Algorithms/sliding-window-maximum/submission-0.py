

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        r = k
        for l in range(len(nums) - k + 1):

            res.append(max(nums[l:r]))
            r+=1
        return res