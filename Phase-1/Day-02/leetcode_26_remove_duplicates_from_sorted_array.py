


# LeetCode 1920 - Remove Duplicates from Sorted Array
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

def removeDuplicates(self, nums: List[int]) -> int:
    k = 1
    for i in range(1 ,len(nums)):
        if nums[i] != nums[ k -1]:
            nums[k] = nums[i]
            k += 1
    return k