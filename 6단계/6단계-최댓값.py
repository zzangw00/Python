arr = []

for i in range(9):
    arr.append(int(input()))

print(max(arr))
print(int(arr.index(max(arr))) + 1)