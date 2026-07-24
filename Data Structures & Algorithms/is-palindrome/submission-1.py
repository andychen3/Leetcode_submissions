class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        lowered_word = s.lower()

        while left < right:
            if not lowered_word[left].isalnum():
                left += 1
            elif not lowered_word[right].isalnum():
                right -= 1
            elif lowered_word[left] != lowered_word[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
                