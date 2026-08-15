


nums = [1, 2, 3, 4, 5, 6]
prefix = []
total = 0

for num in nums:
    total += num
    prefix.append(total)
print(prefix[2])
print(prefix[4] - prefix[0])
print(prefix[5] - prefix[1])