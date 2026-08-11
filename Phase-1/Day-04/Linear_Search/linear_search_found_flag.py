



array = [15,25,35,45]
target = 35

found = False

for num in array:
    if num == target:
        found = True
        break
if found:
    print("Element Found")



array = [15,25,35,45]
target = 100

found = False

for num in array:
    if num == target:
        found = True
if found:
    print("Element Found")
else:
    print("Element Not Found")