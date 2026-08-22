class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0,0,0]

        for n in nums:
            buckets[n] += 1
        i = 0
        for bucket in range(3):
            size = buckets[bucket]
            j = 0
            while j < size:
                nums[i+j] = bucket
                j += 1
            i += size