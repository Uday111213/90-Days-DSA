
nums = [2, 5, 3, 8, 1]
start = 1
end = 3
prefix = []
total = 0

for num in nums:
    total += num
    prefix.append(total)
print(prefix[end] - prefix[start-1])