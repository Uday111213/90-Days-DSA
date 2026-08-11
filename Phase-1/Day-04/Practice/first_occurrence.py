
# Time Complexity: O(n) - Worst Case
# Space Complexity: O(1)

nums = [10, 20, 30, 20, 40, 20]
target = 20

for i in range(len(nums)):
    if nums[i] == target:
        print("First Occurrence at index:",i)
        break

