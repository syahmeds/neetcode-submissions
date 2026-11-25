class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence_len = 0
        nums_set = set(nums)
        for num in nums_set:
            # A number starts a sequence only if its predecessor is missing.
            # This avoids repeatedly exploring the same chain from the middle.
            if (num - 1) not in nums_set:
                current_num = num
                current_chain = 1
                while (current_num + 1) in nums_set:
                    current_num += 1
                    current_chain += 1
                # Update the best length only after measuring a complete chain.
                longest_sequence_len = max(longest_sequence_len, current_chain)
        return longest_sequence_len
