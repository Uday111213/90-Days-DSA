


nums = [5, -8, 3, -2, 4]
prefix = []
total = 0
for num in nums:
    total += num
    prefix.append(total)

minimum = prefix[0]

for n in prefix:
    if n < minimum:
        minimum = n
print(minimum)