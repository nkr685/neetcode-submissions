class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append(':')
            res.append(s)
            res.append('#')
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        res = []
        i = 0
        while i < len(s):
            j = i
            numStr = ''
            while s[j] !=':':
                numStr+=s[j]
                j += 1
            j += 1
            i = j
            strLen = int(numStr)
            decodedStr = ""
            while j < i+strLen:
                decodedStr += s[j]
                j += 1
            if s[j] == '#':
                res.append(decodedStr)
            j += 1
            i = j
        return res
            


