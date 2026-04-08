class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bucket sort

        buckets = [0] * 3

        for num in nums:
            buckets[num] += 1

        # print(bucket)

        i = 0
        for n in range(len(buckets)):
            for j in range(buckets[n]):
                nums[i] = n
                i += 1
    
        
