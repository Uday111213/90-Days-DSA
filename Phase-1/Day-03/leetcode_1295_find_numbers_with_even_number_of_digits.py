
# LeetCode 1295 - Find Numbers with Even Number of Digits
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            convert_string = str(n)
            if len(convert_string) % 2 == 0:
                count += 1
        return count