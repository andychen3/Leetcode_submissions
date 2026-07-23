from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = defaultdict(int)

        for index, num in enumerate(nums):
            diff = target - num
            if diff in mapping:
                return [mapping[diff], index]
            mapping[num] = index
        
        return [None, None]