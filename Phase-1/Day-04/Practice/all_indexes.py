
# Time Complexity = O(n)
# Space Complexity = O(1)

nums = [5, 10, 5, 20, 5, 30]
target = 5

for i in range(len(nums)):
    if nums[i] == target:
        print("Found at index:",i)