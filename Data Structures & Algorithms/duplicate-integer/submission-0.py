class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ctr = set()
        for num in nums:
            if num in ctr:
                return True
            ctr.add(num)
        return False    