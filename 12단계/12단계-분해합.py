n = int(input())
arr = list()

for i in range(1, n + 1):
    sum = 0
    for j in str(i):
        sum += int(j)
    if sum + i == n:
        arr.append(i)

if not arr:
    print(0)
else:
    print(min(arr))
