
# Time Complexity = O(n)
# Space Complexity = O(1)

nums = [23, 5, 67, 12, 89, 34]
minimum_element = nums[0]

for i in range(len(nums)):
    if nums[i] < minimum_element:
        minimum_element = nums[i]
print("Minimum:",minimum_element)
