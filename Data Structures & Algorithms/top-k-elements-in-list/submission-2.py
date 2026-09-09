from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency, O(N) - time
        num_count = Counter(nums)
        # Sorting - O(NlogN) - time
        # num_count = sorted(num_count.items(), key = lambda x : x[1], reverse=True)
        # Space - O(1)
        # return [x[0] for x in num_count][:k]
        # Using min-heap - O(NlogK)
        num_heap = []
        for num, freq in num_count.items():
            heapq.heappush(num_heap, (freq, num))
            if len(num_heap) > k:
                heapq.heappop(num_heap)
        # Space - O(K) for heap            
        return [x[1] for x in num_heap]
