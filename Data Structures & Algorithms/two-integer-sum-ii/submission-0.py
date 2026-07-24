class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        input: array of numbers. Target number to hit 
        output: array with index of the two numbers + 1
        rules:
        1. output is sorted ascending order
        2. Return the answer of the index of two numbers + 1 to it since its one indexed.
        that equals the target. Index 1 has to be less than index 2 and cannot be equal.
        3. One exact valid solution
        4. Must be O(1) space.

        l. r 
        [1,2,3,4]
         0 1 2 3

        l = 0
        r = 1

        1 + 2 = 3

        [1, 2]
        target = 3

        1. initialize a pointer form the left 0 index and pointer from right end of array.
        2. Check if the left and right numbers added together is greater than target
            3. If so decrement right
            4. Elif number is less than target increment left
            5. Else if number equals target we return result array of index of first and second number added 1 each
        6. 

        '''
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]

