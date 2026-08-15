


nums = [3, 1, 4, 2, 5]
prefix = []
total = 0

for num in nums:
    total += num
    prefix.append(total)
print(prefix)