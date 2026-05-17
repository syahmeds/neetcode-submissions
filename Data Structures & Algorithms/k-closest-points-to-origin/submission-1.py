from random import randint
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # dist_points_max_heap = []
        # for x, y in points:
        #     heapq.heappush(dist_points_max_heap, [-(x**2 + y**2), (x, y)])
        #     if len(dist_points_max_heap) > k:
        #         heapq.heappop(dist_points_max_heap)
        # return [[x,y] for _, (x,y) in dist_points_max_heap]
        def swap(i, j):
            points[i], points[j] = points[j], points[i]
        
        def partition(start, end):
            rand = randint(start, end)
            swap(rand, end)
            pivot_dist = points[end][0] ** 2 + points[end][1] ** 2
            i = start
            for j in range(start, end):
                cur_dist = points[j][0] ** 2 + points[j][1] ** 2
                if cur_dist <= pivot_dist:
                    if i != j:
                        swap(i, j)
                    i += 1
            swap(i, end)
            return i
        
        def _kthClosest(start, end):
            part = partition(start, end)
            if k - 1 == part:
                return points[:part+1]
            elif k - 1 < part:
                return _kthClosest(start, part - 1)
            else:
                return _kthClosest(part + 1, end)
        
        return _kthClosest(0, len(points) - 1)
