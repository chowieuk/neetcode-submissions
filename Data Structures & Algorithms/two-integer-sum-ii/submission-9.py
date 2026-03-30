class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        for _ in range(len(numbers)):
            print([left + 1, right + 1], numbers[left], numbers[right])
            while left <= right:
                if numbers[left] + numbers[right] == target:
                        return [left + 1, right + 1]
                right -= 1
            left += 1
            right = len(numbers) - 1

