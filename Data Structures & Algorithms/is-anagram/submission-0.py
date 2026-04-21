class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not (len(s) == len(t)):
            return False
        # Hash-map - dictionary
        # Time - O (M + N) - where M and N are lengths of s and t
        # Space - O (M + N) - where M and N are lengths of s and t    
        char_counter_s = {}
        char_counter_t = {}
        # for c in s:
        #     if c in char_counter_s:
        #         char_counter_s[c] += 1
        #     else:
        #         char_counter_s[c] = 1

        # for c in t:
        #     if c in char_counter_t:
        #         char_counter_t[c] += 1
        #     else:
        #         char_counter_t[c] = 1
        # for i in range(len(s)):
        #     char_counter_s[s[i]] = char_counter_s.get(s[i], 0) + 1
        #     char_counter_t[t[i]] = char_counter_t.get(t[i], 0) + 1
        # return char_counter_s == char_counter_t 
        # Hash table - using fixed array
        # Time - O(M + N) - where M and N are lengths of s and t
        # Space - O(1) - array size is fixed
        char_counter = [0] * 52
        for i in range(len(s)):
            char_counter[ord(s[i]) - ord('a')] += 1
            char_counter[ord(t[i]) - ord('a')] -= 1

        for val in char_counter:
            if val != 0:
                return False

        return True                   