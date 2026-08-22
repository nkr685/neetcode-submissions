class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums)*2)
        for i, a in enumerate(nums):
            ans[i] = a
            ans[i+len(nums)] = a
        return ans