


nums = [5, -3, 2, -4, 6]
prefix = []
total = 0

for num in nums:
    total += num
    prefix.append(total)
print(prefix)