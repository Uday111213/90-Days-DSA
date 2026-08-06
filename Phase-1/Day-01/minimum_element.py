


# Find the minimum element.


l = [4,3,5,66,55,0,44,-98]

smallest = l[0]
for num in l:
    if num < smallest:
        smallest = num
print("Smallest is:",smallest)
