

# Time Complexity = O(n)
# Space Complexity = O(1)

nums = [3, 4, 5, 2, 4, 22, 55]
target = 4

for i in range(len(nums)):
    if nums[i] == target:
        print("Index:",i)