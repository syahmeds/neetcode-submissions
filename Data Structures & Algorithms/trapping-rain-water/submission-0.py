class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0
        # Brute force:
        # Time - O(N^2)
        # Space - O(1)
        # for i in range(n):
        #     left_max = right_max = height[i]

        #     for j in range(i):
        #         left_max = max(left_max, height[j])
            
        #     for j in range(i+1, n):
        #         right_max = max(right_max, height[j])
            
        #     res += min(left_max, right_max) - height[i]

        # return res
        # Multiple passes
        # Left max and right max arrays
        # Time - O(N)
        # Space - O(N)
        # left_max = [0] * n
        # right_max = [0] * n
        # left_max[0] = height[0]
        # for i in range(1,n):
        #     left_max[i] = max(left_max[i-1], height[i])
        # right_max[n-1] = height[n-1]
        # for i in range(n-2,-1,-1):
        #     right_max[i] = max(right_max[i+1], height[i])
        # for i in range(n):
        #     res += min(left_max[i], right_max[i]) - height[i]
        # return res
        l, r = 0, n-1
        left_max, right_max = 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    res += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    res += right_max - height[r]
                r -= 1
        return res
        