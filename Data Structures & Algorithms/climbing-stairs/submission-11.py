class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        def dfs(i: int):
            if i <= 2:
                return i
            if i-1 not in d:
                d[i-1] = dfs(i-1)
            if i-2 not in d:
                d[i-2] = dfs(i-2)
            return d[i-1] + d[i-2]
        
        return dfs(n)