class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC = 0
        curC = 0
        for n in nums:
            if n == 1:
                curC += 1
                maxC = max(maxC, curC)
            else:
                curC = 0
        return maxC