class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sorting
        # Complexity: where M is number of strings and N is length of longest string
        # Time: O(M * NlogN)
        # Space: O(M * N)
        # anagram_map = defaultdict(list)
        # for str in strs:
        #     anagram_map[tuple(sorted(str))].append(str)
        # return list(anagram_map.values())
        # Using frequency array, can be used if input char count is fixed - example lowercase english letters etc.
        # Complexity: where M is number of strings and N is length of longest string
        # Time: O(M*N)
        # Space: O(M) aux space, excluding returned output -> O(M*N) total space if output groups are counted
        anagram_map = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] += 1
            anagram_map[tuple(count)].append(str)
        return list(anagram_map.values())