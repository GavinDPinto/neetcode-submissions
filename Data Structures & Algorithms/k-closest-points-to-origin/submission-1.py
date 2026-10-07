class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(pq, (dist, point))
        
        ret = []

        for i in range(k):
            ret.append(heapq.heappop(pq)[1])
        
        return ret