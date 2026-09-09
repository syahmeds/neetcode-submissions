from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        num_count = sorted(num_count.items(), key = lambda x: x[1], reverse=True)
        return [x[0] for x in num_count[:k]]