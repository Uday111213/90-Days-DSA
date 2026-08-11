
# Time Complexity: O(n)
# Space Complexity: O(1)

nums = [10, 20, 30, 20, 40, 50]
target = 20
remember_index = -1

for i in range(len(nums)):
    if nums[i] == target:
        remember_index = i
print("Last occurrence at index:",remember_index)