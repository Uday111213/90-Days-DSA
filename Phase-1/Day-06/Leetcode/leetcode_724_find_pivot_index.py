


# LeetCode 724 - Find Pivot Index
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)

        for i in range(len(nums)):
            if i == 0:
                left_sum = 0
            else:
                left_sum = prefix[i - 1]

            right_sum = total - prefix[i]

            if left_sum == right_sum:
                return i
        return -1
