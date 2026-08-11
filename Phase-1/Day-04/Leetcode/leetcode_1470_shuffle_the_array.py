
# LeetCode 1470 - Shuffle the Array
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)


from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result