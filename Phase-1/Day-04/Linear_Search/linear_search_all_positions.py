

# Time Complexity = O(n)
# Space Complexity = O(1)


arr =  [10, 20, 30, 20, 40, 20]
target = 20

for i  in range(len(arr)):
    if arr[i] == target:
        print("Found at index:",i)