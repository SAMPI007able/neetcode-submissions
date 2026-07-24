import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for idx, point in enumerate(points):
            distance_origin = abs(point[1])**2 + abs(point[0])**2
            heapq.heappush(heap, (-distance_origin, idx))
            if len(heap) > k:
                heapq.heappop(heap)
        # print(heap)
        while heap:
            result.append( points[heapq.heappop(heap)[1]] )
        return result