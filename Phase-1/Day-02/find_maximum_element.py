

# Time Complexity = O(n)
# Space Complexity = O(1)


numbers = [29,43,34,45,34]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Maximum Element is:",largest)