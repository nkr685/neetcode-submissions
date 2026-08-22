class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = "-1:-:#+#"
        for s in strs:
            encodedStr += str(len(s))+':-:' + s + "#+#"
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decoded = []
        print(s.split('#'))
        for encodedStr in s.split('#+#')[:-1]:
            print(encodedStr)
            numS, s = encodedStr.split(':-:')
            num = int(numS)
            if num == -1:
                continue
            else:
                decoded.append(s)
        return decoded
