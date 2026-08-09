

# LeetCode 485 - Max Consecutive Ones
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
       count = 0
       maximum_streak = 0
       for n in nums:
            if n == 1:
                count += 1
                if count > maximum_streak:
                    maximum_streak = count
            else:
                count = 0
       return maximum_streak