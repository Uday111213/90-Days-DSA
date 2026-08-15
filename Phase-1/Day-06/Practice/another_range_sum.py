


nums = [10, 20, 30, 40, 50]
start = 2
end = 4
prefix = []
total = 0

for num in nums:
    total += num
    prefix.append(total)
print(prefix[end] - prefix[start-1])