

# Time Complexity = O(n)
# Space Complexity = O(1)


nums = [10, 20, 20, 30, 20]
target = 20
count = 0

for num in nums:
    if num == target:
        count += 1
print("Count is:",count)
