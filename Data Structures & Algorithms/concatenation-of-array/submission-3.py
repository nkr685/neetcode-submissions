class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [0] * ( 2 * nums_len )
        print(len(ans))
        for i, num in enumerate(nums):
            ans[i] = num
            ans[i+nums_len] = num
        return ans