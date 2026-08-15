


nums = [5, 10, 15, 20]
prefix = []
total = 0

for i in range(len(nums)):
    total += nums[i]
    prefix.append(total)
print(prefix)