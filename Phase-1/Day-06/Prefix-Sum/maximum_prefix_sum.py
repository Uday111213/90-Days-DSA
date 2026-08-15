


nums = [2, -1, 5, -3, 4]
prefix = []
total = 0
for num in nums:
    total += num
    prefix.append(total)

maximum = prefix[0]

for n in prefix:
    if n > maximum:
        maximum = n
print(maximum)