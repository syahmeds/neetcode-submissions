class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time - O(m x n)
        # Space - O(m x n)
        # m is length of longest str in strs, n is number of strs
        # res = defaultdict(list)
        # for str in strs:
        #     char_counter = [0] * 26
        #     for c in str:
        #         char_counter[ord(c) - ord('a')] += 1
        #     res[tuple(char_counter)].append(str)
        # return list(res.values())        
        # Time - O(m x nlogn)
        # Space - O(m x n)
        res = defaultdict(list)
        for str in strs:
            sortedStr = ''.join(sorted(str))
            res[sortedStr].append(str)
        return list(res.values())    