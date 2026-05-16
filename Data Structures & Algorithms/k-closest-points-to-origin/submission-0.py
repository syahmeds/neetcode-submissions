class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_points_max_heap = []
        for x, y in points:
            heapq.heappush(dist_points_max_heap, [-(x**2 + y**2), (x, y)])
            if len(dist_points_max_heap) > k:
                heapq.heappop(dist_points_max_heap)
        return [[x,y] for _, (x,y) in dist_points_max_heap]