


nums = [4, 2, 7, 1, 5]
end = 3
prefix = []
total = 0

for num in nums:
    total += num
    prefix.append(total)
print(prefix[3])