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
        # Time - O(NlogN (sort) + N^2) => O(N^2)
        # Space - O(1) (assuming sorting doesn't use merge sort and uses quick sort instead)
        def two_sum_all_pairs(arr, start, target):
            pairs = []
            left, right = start, len(arr) - 1
            while left < right:
                cur_sum = arr[left] + arr[right]
                if cur_sum == target:
                    pairs.append([arr[left], arr[right]])
                    left += 1
                    while left < right and arr[left] == arr[left-1]:
                        left += 1
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1
            return pairs

        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pairs = two_sum_all_pairs(nums, i+1, -nums[i])
            for pair in pairs:
                triplets.append([nums[i]] + pair)            
        return triplets