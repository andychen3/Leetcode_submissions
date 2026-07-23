from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = Counter(nums)
        return [val for val, count in top_k.most_common(k)]
        
