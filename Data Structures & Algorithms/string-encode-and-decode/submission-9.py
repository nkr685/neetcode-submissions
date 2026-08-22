class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        firstPass  = True
        for s in strs:
            if firstPass:
                encodedStr = s
                firstPass = False
            else:
                encodedStr += ',-,' + s
        return str(len(strs)) + ':' + encodedStr

    def decode(self, s: str) -> List[str]:
        print(s)
        num, decoded = s.split(':', 1)
        if num == '0':
            return []
        return decoded.split(',-,')
