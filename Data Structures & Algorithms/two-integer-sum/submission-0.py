
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if (seen.get(difference, None) != None):
                return [seen.get(difference), i]
            else:
                seen[nums[i]] = i
                continue