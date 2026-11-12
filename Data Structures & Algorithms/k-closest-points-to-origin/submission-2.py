import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distances.append((math.sqrt((point[0]**2)+(point[1]**2)), point))
        distances.sort(key=lambda x: x)
        return [distances[i][1] for i in range(k)]