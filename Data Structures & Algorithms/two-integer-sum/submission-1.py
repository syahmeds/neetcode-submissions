class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nested for loop
        # Time: O(N^2)
        # Space: O(1)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return [-1,-1]
         # Sort and compare
        # Time - O(N) + O(NlogN) => O(NlogN)
        # Space - O(1) if sort doesn't use extra space
        # nums = [(num,idx) for (idx,num) in enumerate(nums)]
        # nums.sort()
        # n = len(nums)
        # l, r = 0, n-1
        # while l < r:
        #     total = nums[l][0] + nums[r][0]
        #     if total == target:
        #         i, j = nums[l][1], nums[r][1]
        #         return [min(i,j), max(i,j)]
        #     elif total < target:
        #         l += 1
        #     else:
        #         r -= 1
        # Using hash-map
        # Time: O(N)
        # Space: O(N)
        num_map = {}
        for (idx, num) in enumerate(nums):
            goal = target - num
            if goal in num_map:
                return [num_map[goal], idx]
            else:
                num_map[num] = idx
        return [-1,-1]