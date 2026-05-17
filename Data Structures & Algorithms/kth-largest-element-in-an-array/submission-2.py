from random import randint
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for num in nums:
            heapq.heappush(res, num)
            if len(res) > k:
                heapq.heappop(res)
        return res[0]
        

        # Quickselect
        # Time - O(N)
        # Space - O(1)
        # def swap(i, j):
        #     nums[i], nums[j] = nums[j], nums[i]
        
        # def partition(start, end):
        #     rand = randint(start, end)
        #     swap(rand, end)
        #     pivot = nums[end]
        #     i = start
        #     for j in range(start, end):
        #         if nums[j] > pivot:
        #             swap(i, j)
        #             i += 1
        #     swap(i, end)
        #     return i
        
        # def _findKthLargest(start, end):
        #     part = partition(start, end)
        #     if k - 1 == part:
        #         return nums[part]
        #     elif k - 1 < part:
        #         return _findKthLargest(start, part - 1)
        #     else:
        #         return _findKthLargest(part + 1, end)
        
        # return _findKthLargest(0, len(nums) - 1)