
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # val -> index
        for i, v in enumerate(nums):
            difference = target - v
            if difference in seen:
                return [seen.get(difference), i]
            else:
                seen[v] = i
                continue