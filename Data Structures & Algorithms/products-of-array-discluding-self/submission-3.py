class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            if i-1 >= 0:
                prefix *= nums[i-1]
            res.append(prefix)
        for i in range(len(nums)-1, -1, -1):
            if i+1 < len(nums):
                postfix *= nums[i+1]
            res[i] *= postfix
        return res