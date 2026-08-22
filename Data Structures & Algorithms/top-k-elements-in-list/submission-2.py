class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        topK = {}
        for n in nums:
            if n in freqs.keys():
                freqs[n] += 1
            else:
                freqs[n] = 1
        for key, val in freqs.items():
            if val in topK.keys():
                topK[val].append(key)
            else:
                topK[val] = [key]
        sortedK = []
        for key in reversed(sorted(topK.keys())):
            for num in topK[key]:
                sortedK.append(num)
            if len(sortedK) == k:
                break
        return sortedK
