

# Time Complexity = O(n)
# Space Complexity = O(1)


fruits = ["apple", "banana", "mango", "orange"]
target = "mango"

for i in range(len(fruits)):
    if fruits[i] == target:
        print("Index:",i)