

# Time Complexity = O(n)
# Space Complexity = O(1)


numbers = [29,43,34,45,34]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Minimum Element is:",smallest)