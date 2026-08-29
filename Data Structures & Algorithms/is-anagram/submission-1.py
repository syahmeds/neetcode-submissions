class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        # Time: Sort - O(NLogN) + Compare - O(N) => O(NLogN)
        # Space: If sort is quick-sort then O(1) I guess => O(1)
        # s = sorted(s)
        # t = sorted(t)
        # return s == t
        # Time: O(N) - iterate and collect in hashmap + compare - O(N) => O(N)
        # Space: O(N) - for 2 hashmaps
        # from collections import Counter
        # s_ctr = Counter(s)
        # t_ctr = Counter(t)
        # return s_ctr == t_ctr
        # Time - O(N)
        # Space - O(1)
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i])- ord('a')] -= 1
        for val in count:
            if not val == 0:
                return False
        return True