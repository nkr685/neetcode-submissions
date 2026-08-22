class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = None
        zeroes = 0
        products = []
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                zeroes += 1
            else:
                if total == None:
                    total = num
                else:
                    total *= num
        if zeroes > 1:
            return [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if zeroes > 0:
                if nums[i] == 0:
                    products.append(total)
                else:
                    products.append(0)
            else:
                products.append(int(total/nums[i]))
        return products