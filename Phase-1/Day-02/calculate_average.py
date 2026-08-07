
# Time Complexity = O(n)
# Space Complexity = O(1)



numbers = [32,3,54,3,6]
total = 0
for num in numbers:
    total += num
avg = total/len(numbers)
print("Average:",avg)


                # or


numbers = [32,3,54,3,6]
total = sum(numbers)
avg = total/len(numbers)
print("Average:",avg)