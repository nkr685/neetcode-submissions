class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        for n in nums:
            if n != val:
                nums[p] = n
                p += 1
        return p