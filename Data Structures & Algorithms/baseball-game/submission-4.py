class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = 0
        s = []
        for op in operations:
            if op == '+':
                total = s[-1] + s[-2]
                x += total
                s.append(total)
            elif op == 'C':
                x -= s.pop()
            elif op == 'D':
                result = s[-1]*2
                s.append(result)
                x += result
            else:
                s.append(int(op))
                x += (int(op))
        return x