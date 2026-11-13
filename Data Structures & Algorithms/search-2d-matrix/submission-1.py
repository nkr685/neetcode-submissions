class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix) - 1
        c = 0
        while u <= d:
            c = (u + d) // 2
            if target < matrix[c][0]:
                d = c - 1
            elif target > matrix[c][0]:
                if target <= matrix[c][-1]:
                    break
                u = c + 1
            else:
                return True
        
        l, r = 0, len(matrix[c]) - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[c][m]:
                r = m - 1
            elif target > matrix[c][m]:
                l = m + 1
            else:
                return True            
        return False