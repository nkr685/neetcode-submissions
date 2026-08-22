class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        total = 0
        for op in operations:
            idx = len(res)
            print(res)
            match op:
                case "+":
                    sum = int(res[idx-1])+int(res[idx-2])
                    total += sum
                    res.append(str(sum))
                    continue
                case "C":
                    dif = res.pop()
                    total -= int(dif)
                    continue
                case "D":
                    d = int(res[idx-1])*2
                    total += d
                    res.append(str(d))
                    continue
                case _:
                    total += int(op)
                    res.append(op)
        
        return total
