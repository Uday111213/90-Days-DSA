


# LeetCode 1929 - Concatenation of Array
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = nums.copy()
        final_result = nums + result
        return final_result