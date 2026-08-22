class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for c1,c2 in zip(sorted(s),sorted(t)):
            if c1 is not c2:
                return False
        return True