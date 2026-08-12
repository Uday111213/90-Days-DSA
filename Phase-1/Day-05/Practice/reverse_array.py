

# Time Complexity = O(n)
# Space Complexity = O(n)

nums = [10,20,30,40,50]
result = []

for i in range(len(nums)-1,-1,-1):
    result.append(nums[i])
print(result)