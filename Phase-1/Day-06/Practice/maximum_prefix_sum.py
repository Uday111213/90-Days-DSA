


nums = [3, 1, 4, 2, 5]
prefix = []
total = 0

for num in nums:
    total += num
    prefix.append(total)
print(prefix)

maximum = prefix[0]
for n in prefix:
    if n > maximum:
        maximum = n
print(maximum)