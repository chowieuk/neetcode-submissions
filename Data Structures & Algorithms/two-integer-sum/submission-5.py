class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + num[j] == target; i != j

        # Algorithm:
        # Calculate the diff of the target and our number
        # If the diff is in our map of diff to index
        #   return [value of the map, current index]
        # Store the diff in our map of diff to index
        seen = {}
        # seen is a map of diff to index
        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], index]
            seen[num] = index