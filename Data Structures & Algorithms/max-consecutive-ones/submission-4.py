class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC = 0
        curC = 0
        for i in nums:
            if i == 1:
                curC += 1
            else:
                if curC > maxC:
                    maxC = curC
                curC = 0
        return max(maxC, curC)