

# Find the largest element in a list.

numbers = [12,3,4,1,6]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
print("Largest is: ",largest)
