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
            while s[j] !=':':
                j += 1
            strLen = int(s[i:j])
            j += 1
            i = j
            decodedStr = s[i:j+strLen]
            res.append(decodedStr)
            j += 1
            i = j+strLen
        return res
            


