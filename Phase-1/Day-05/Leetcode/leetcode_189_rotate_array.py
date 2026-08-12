
# LeetCode 189 - Rotate Array
# Difficulty: Medium
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%= len(nums)
        nums[:] = nums[-k:] + nums[:-k]