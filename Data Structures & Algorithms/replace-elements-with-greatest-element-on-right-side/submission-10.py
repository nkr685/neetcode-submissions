class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        h = arr[-1]
        arr[-1] = -1
        i = len(arr) - 2
        while i >= 0:
            if arr[i] <= h:
                arr[i] = h
            else:
                tmp = arr[i]
                arr[i] = h
                h = tmp
            i -= 1
        return arr