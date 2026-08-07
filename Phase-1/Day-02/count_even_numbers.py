

# Time Complexity = O(n)
# Space Complexity = O(1)


numbers = [2,3,5,4,66,55,3]
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print("Even Count is:",count)