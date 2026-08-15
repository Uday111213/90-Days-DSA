

user_input = map(int,input("Enter numbers:").split())
prefix = []
total = 0

for num in user_input:
    total += num
    prefix.append(total)
print("Prefix Sum:",prefix)