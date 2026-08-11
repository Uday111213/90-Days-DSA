

# Time Complexity = O(n)
# Space Complexity = O(1)


nums = [10, 20, 30, 40, 50]
target = 40

for i in range(len(nums)):
    if nums[i] == target:
        print("Index:",i)