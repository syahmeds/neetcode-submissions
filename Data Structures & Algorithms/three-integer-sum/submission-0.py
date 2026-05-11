class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time - O(N^3)
        # Space - O(N)
        # res = set()
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             test = nums[i] + nums[j] + nums[k]
        #             if test == 0:
        #                 res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        # return list(res)
        nums.sort()
        res = []
        n = len(nums)
        i = 0
        while i < n:
            a = nums[i]
            if a > 0:
                break
            l, r = i + 1, n - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
            i += 1
            while i < n and nums[i-1] == nums[i]:
                i += 1
        return res