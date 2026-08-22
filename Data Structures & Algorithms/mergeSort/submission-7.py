# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) == 1:
            return pairs
        elif len(pairs) == 0:
            return []
        m = len(pairs) // 2

        left = self.mergeSort(pairs[0:m])
        right = self.mergeSort(pairs[m:len(pairs)])

        return self.merge(left, right)

    def merge(self, leftPairs: List[Pair], rightPairs: List[Pair]):
        sorted = []
        while leftPairs or rightPairs:
            if not leftPairs:
                sorted.append(rightPairs.pop(0))
            elif not rightPairs:
                sorted.append(leftPairs.pop(0))
            elif leftPairs[0].key < rightPairs[0].key:
                sorted.append(leftPairs.pop(0))
            elif leftPairs[0].key > rightPairs[0].key:
                sorted.append(rightPairs.pop(0))
            else:
                sorted.append(leftPairs.pop(0))
                sorted.append(rightPairs.pop(0))
        return sorted








