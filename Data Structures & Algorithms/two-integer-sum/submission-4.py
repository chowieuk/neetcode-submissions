class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + num[j] == target; i != j

        # Algorithm:
        # Calculate the diff of the target and our number
        # If the diff is in our map of diff to index
        #   return the an array of value of the map, current index
        # Store the diff in our map of diff to index
        seen = {}
        for i, v in enumerate(nums):
            diff = target - v
            if v in seen:
                return [seen[v], i]
            seen[diff] = i