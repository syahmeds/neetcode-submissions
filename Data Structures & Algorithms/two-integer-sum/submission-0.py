class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(N^2) - time
        # O(1) - space
        # for i in range(len(nums)):
            # for j in range(1,len(nums)):
                # if nums[i] + nums[j] == target:
                    # return [i, j]
        # return []            

        # O(N) - time
        # O(N) - space
        # num_hash = {}
        # for i in range(len(nums)):
        #     difference = target - nums[i]
        #     if difference in num_hash:
        #         return [num_hash[difference], i]
        #     else:
        #         num_hash[nums[i]] = i
        # 2 - pointer
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])    

        A.sort()

        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]    
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1

        return []            