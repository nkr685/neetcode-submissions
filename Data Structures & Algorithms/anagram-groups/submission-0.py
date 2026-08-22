class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = []
        groups = []
        for s in strs:
            key = sorted(s)
            if key not in keys:
                keys.append(key)
                groups.append([s])
            else:
                groups[keys.index(key)].append(s)
        return groups