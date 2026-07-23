from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = defaultdict(list)

        for word in strs:
            key = tuple(sorted(list(word)))
            sublists[key].append(word)
        
        return list(sublists.values())