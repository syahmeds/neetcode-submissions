class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(x,i) for (i,x) in enumerate(nums)]
        nums.sort()
        n = len(nums)
        i, j = 0, n-1
        while i < j:
            l,r = nums[i], nums[j]
            cur_sum = l[0] + r[0]
            if cur_sum == target:
                return [min(l[1],r[1]), max(l[1],r[1])]
            elif cur_sum > target:
                j -= 1
            else:
                i += 1