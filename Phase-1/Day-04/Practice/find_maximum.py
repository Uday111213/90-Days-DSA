
# Time Complexity = O(n)
# Space Complexity = O(1)

nums = [23, 5, 67, 12, 89, 34]
maximum_element = nums[0]

for i in range(len(nums)):
    if nums[i] >maximum_element:
        maximum_element = nums[i]
print("Maximum:",maximum_element)
