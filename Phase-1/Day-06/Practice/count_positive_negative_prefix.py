

nums = [3, -5, 4, 2, -1]
prefix = []
total = 0

for num in nums:
    total += num
    prefix.append(total)
print(prefix)

zero_count = 0
positive_count = 0
negative_count = 0
for n in prefix:
    if n == 0:
        zero_count += 1
    elif n > 0:
        positive_count += 1
    else:
        negative_count += 1
print("Zero count is:",zero_count)
print("Positive count is:",positive_count)
print("Negative count is:",negative_count)