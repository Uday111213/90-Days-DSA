

# Time Complexity = O(n)
# Space Complexity = O(1)


array = list(map(int,input("Enter Array:").split(",")))
target = int(input("Enter target:"))
count = 0

for num in array:
    if num == target:
        count += 1
print("Count:",count)