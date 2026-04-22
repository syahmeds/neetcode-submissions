class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_ctr = defaultdict(int)
        for num in nums:
            freq_ctr[num] += 1
        res = [] 
        for key, val in freq_ctr.items():
            res.append((val, key))
        res.sort(reverse=True)
        return [j for (i,j) in res[:k]]    