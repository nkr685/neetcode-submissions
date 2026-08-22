class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        loweredS = s.lower()
        while True:
            while i < j and not loweredS[i].isalpha() and not loweredS[i].isdigit():
                i += 1
            while j > i and not loweredS[j].isalpha() and not loweredS[j].isdigit():
                j -= 1
            if loweredS[i] != loweredS[j]:
                return False
            if i == j or i + 1 == j:
                return True
            i += 1
            j -= 1
        return True