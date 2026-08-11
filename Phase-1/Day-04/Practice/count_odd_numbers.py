
# Time Complexity = O(n)
# Space Complexity = O(1)

nums = [10, 15, 22, 33, 40, 51, 64]
count = 0

for num in nums:
    if num % 2 != 0:
        count += 1
print("Odd count:",count)