class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newList = []
        for num in nums:
            if newList.__contains__(num):
                return True
            newList.append(num)
        return False  