
# Time Complexity = O(n)
# Space Complexity = O(1)


nums = [10, 20, 30, 40, 50]
target = 60
found = False
for num in nums:
    if num == target:
        found = True
if found:
    print("Element Found")
else:
    print("Element not found")