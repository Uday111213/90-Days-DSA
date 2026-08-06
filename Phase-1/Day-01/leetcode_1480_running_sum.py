
# LeetCode 1480 - Running Sum of 1D Array
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        current_sum = 0
        for i in nums:
            current_sum += i
            result.append(current_sum)
        return result