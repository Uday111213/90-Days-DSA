

# Time Complexity = O(n)
# Space Complexity = O(1)


array_size = int(input("Enter Array size: "))
array_elements = list(map(int,input("Enter Array elements: ").split()))
target_element = int(input("Enter Target element: "))

for num in array_elements:
    if num == target_element:
        print("Element Found")