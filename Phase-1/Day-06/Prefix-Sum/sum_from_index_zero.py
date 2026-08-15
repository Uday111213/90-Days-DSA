


nums = [2, 4, 3, 5, 1]
end = 3
prefix = []
total = 0

for num in nums:
    total += num
    prefix.append(total)

print(prefix[end])
