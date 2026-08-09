


# Time Complexity = O(n)
# Space Complexity = O(1)

numbers = [3,4,3,5,322,5,6]

for i in range(len(numbers)):
    if (i+1) % 2 == 0:
        print(numbers[i])
