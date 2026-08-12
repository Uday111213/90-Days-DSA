
# Time Complexity = O(n)
# Space Complexity = O(n)

nums = [1,2,3,4,5]
k = 2

result = nums[k:] + nums[:k]
print(result)