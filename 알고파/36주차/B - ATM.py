n = int(input())
arr = list(map(int, input().split()))
sum = 0
arr.sort()
for i in range(n):
    for j in range(i + 1):
        sum += arr[j]
print(sum)