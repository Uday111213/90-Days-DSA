

# Time Complexity = O(n)
# Space Complexity = O(1)

numbers = [3,4,22,32,1,43,5]

for i in range(len(numbers)):
    if (i+1) % 2 !=0:
        print(numbers[i])