



nums = [5, -2, 3, -1, 4]
prefix = []
total = 0

for num in nums:
    total += num
    prefix.append(total)
print(prefix)
