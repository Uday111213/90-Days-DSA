
# LeetCode 1431 - Kids With the Greatest Number of Candies
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)


from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = candies[0]
        result = []
        for i in range(len(candies)):
            if candies[i] > maximum:
                maximum = candies[i]
        for candy in candies:
            add = candy + extraCandies
            if add >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result